/**
 * @file Program.cs
 * @brief This file defines the entry point for the application.
 */

namespace AgentOrchestration.App
 {
    using AgentOrchestration.Agents;
    using Microsoft.Extensions.DependencyInjection;
    using Microsoft.Extensions.Hosting; // Add this line
    using Microsoft.Extensions.Logging;

    /// <summary>
    /// The entry point for the application.
    /// </summary>
    public static class Program
    {
        /// <summary>
        /// The entry point for the application.
        /// </summary>
        /// <param name="args"></param>
        public static async Task Main(string[] args)
        {
            var hostBuilder = Host.CreateDefaultBuilder(args)
                .UseConsoleLifetime()
                .ConfigureServices((hostContext, services) =>
                {
                    ConfigureServices(services);
                });
            
            var host = hostBuilder.Build();
            await host.RunAsync();
        }

        /// <summary>
        /// Configures the application's services.
        /// </summary>
        private static void ConfigureServices(IServiceCollection services)
        {
            services.AddLogging(c => c.AddConsole().SetMinimumLevel(LogLevel.Trace));
            services.RegisterSemanticKernel();
            services.AddHostedService<AgentOrchestrationService>();
        }
    }
 }