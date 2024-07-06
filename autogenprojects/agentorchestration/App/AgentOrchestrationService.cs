/**
 * @file AgentOrchestrationService.cs
 * @brief This file defines the AgentOrchestrationService class.
 */

namespace AgentOrchestration.App
{
    using AgentOrchestration.Agents;
    using Microsoft.Extensions.DependencyInjection;
    using Microsoft.Extensions.Hosting;
    using Microsoft.Extensions.Logging;

    /// <summary>
    /// The AgentOrchestrationService class.
    /// </summary>
    public class AgentOrchestrationService : IHostedService
    {
        /// <summary>
        /// The logger.
        /// </summary>
        private readonly ILogger<AgentOrchestrationService> logger;

        private readonly IServiceProvider serviceProvider;

        /// <summary>
        /// Initializes a new instance of the AgentOrchestrationService class.
        /// </summary>
        /// <param name="logger"></param>
        public AgentOrchestrationService(
            ILogger<AgentOrchestrationService> logger,
            IServiceProvider serviceProvider)
        {
            this.logger = logger;
            this.serviceProvider = serviceProvider;
        }

        public async Task StartAsync(CancellationToken cancellationToken)
        {
            this.logger.LogInformation("AgentOrchestrationService started.");

            var lightManager = this.serviceProvider.GetRequiredService<LightManager>();
            await lightManager.Run();
        }

        public Task StopAsync(CancellationToken cancellationToken)
        {
            this.logger.LogInformation("AgentOrchestrationService stopped.");
        
            // Add any necessary code here.
        
            return Task.CompletedTask;
        }
    }
}