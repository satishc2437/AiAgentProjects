

using System.Diagnostics;
using Microsoft.Extensions.Logging;
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.ChatCompletion;
using Microsoft.SemanticKernel.Connectors.OpenAI;


/**
 * @file LightManager.cs
 * @brief Manages the lights in the environment.
 */
namespace AgentOrchestration.Agents
{
    public class LightManager
    {
        private readonly ILogger<LightManager> logger;
        private readonly IChatCompletionService chatCompletionService;
        private readonly Kernel kernel;

        public LightManager(
            ILogger<LightManager> logger,
            IChatCompletionService chatCompletionService,
            Kernel kernel)
        {
            this.logger = logger;
            this.chatCompletionService = chatCompletionService;
            this.kernel = kernel;
        }

        public async Task Run()
        {
            this.logger.LogInformation("LightManager started.");
            var chatCompletionService1 = this.kernel.GetRequiredService<IChatCompletionService>();
            var chatCompletionService2 = this.chatCompletionService;

            Debug.Assert(chatCompletionService1 == chatCompletionService2, "ChatCompletionService instances are not the same.");

            // Enable planning
            OpenAIPromptExecutionSettings openAIPromptExecutionSettings = new()
            {
                ToolCallBehavior = ToolCallBehavior.AutoInvokeKernelFunctions
            };
            var history = new ChatHistory();

            history.AddSystemMessage("You are a helpful assistant. You manage the lights in the environment.");

            // Initiate a back-and-forth chat
            string? userInput;
            do
            {
                // Collect user input
                Console.Write("User > ");
                userInput = Console.ReadLine();

                // Add user input
                history.AddUserMessage(userInput);

                try
                {
                    // Get the response from the AI
                    var result = await this.chatCompletionService.GetChatMessageContentAsync(
                        history,
                        executionSettings: openAIPromptExecutionSettings,
                        kernel: this.kernel);

                    var result2 = await chatCompletionService1.GetChatMessageContentAsync(
                        history,
                        executionSettings: openAIPromptExecutionSettings,
                        kernel: this.kernel);

                    // Print the results
                    Console.WriteLine("Assistant > " + result);
                    Console.WriteLine("Assistant2 > " + result2);

                    // Add the message from the agent to the chat history
                    history.AddMessage(result.Role, result.Content ?? string.Empty);
                }
                catch (Exception ex)
                {
                    Console.WriteLine("An error occurred: " + ex.Message);
                }
            } while (userInput is not null);

            this.logger.LogInformation("LightManager stopped.");
        }
    }
}
