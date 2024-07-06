/**
 * @file SemanticsKernelExtensions.cs
 * @brief This file defines extension methods for SemanticsKernel.
 */

namespace AgentOrchestration.Agents
{
    using Microsoft.Extensions.DependencyInjection;
    using Microsoft.SemanticKernel;

    /// <summary>
    /// Extension methods for SemanticsKernel.
    /// </summary>
    public static class SemanticsKernelExtensions
    {
        public static void RegisterSemanticKernel(this IServiceCollection serviceCollection)
        {
#pragma warning disable SKEXP0010 // Type is for evaluation purposes only and is subject to change or removal in future updates. Suppress this diagnostic to proceed.
            serviceCollection.AddKernel()
                            .AddOpenAIChatCompletion(                
                                modelId: "llama3",
                                apiKey: "ollama",
                                endpoint: new Uri("http://localhost:11434")
                            )
                            .Services.RegisterPlugins();
#pragma warning restore SKEXP0010 // Type is for evaluation purposes only and is subject to change or removal in future updates. Suppress this diagnostic to proceed.
        
            serviceCollection.AddTransient<LightManager>();
        }

        private static void RegisterPlugins(this IServiceCollection services)
        {
            // Add any necessary code here.
            services.AddSingleton(sp => {
                return KernelPluginFactory.CreateFromType<LightsPlugin>("Lights");
            });
        }
    }
}
