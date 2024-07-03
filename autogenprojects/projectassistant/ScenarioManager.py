# This file implements a Manager that creates a new Scenario instance and starts it.

# Path: ScenarioManager.py

from Scenarios.StockMarketAnalysis import StockMarketAnalysisScenario

# ScenarioManager Class
# This class is responsible for managing different scenarios.
# It provides a method to start a specific scenario based on the scenario name provided.
class ScenarioManager:

    # start_scenario Method
    # This method takes a scenario name as input and starts the corresponding scenario.
    # It uses pattern matching to determine which scenario to start.
    # Parameters:
    #   scenario_name (str): The name of the scenario to start.
    # Returns:
    #   The result of the scenario's run method if the scenario is found.
    #   Raises ValueError if the scenario is not found.
    def start_scenario(self, scenario_name):
        match scenario_name:
            case "stock_market_analysis":
                return StockMarketAnalysisScenario().run()
            case _:
                raise ValueError(f"Scenario {scenario_name} not found")