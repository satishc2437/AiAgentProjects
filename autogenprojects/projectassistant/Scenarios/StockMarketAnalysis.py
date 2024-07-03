# This file implements the StockMarketAnalysis scenario.

# Path: Scenarios/StockMarketAnalysis.py

# Importing the required libraries
from Agents.AgentManager import AgentManager

class StockMarketAnalysisScenario:
    def __init__(self):
        self.AgentManager = AgentManager()
        self.UserProxyAgent = self.AgentManager.get_dev_proxy_agent()
        self.StockMarketAssistantAgent = self.AgentManager.get_agent("stock_market_assistant")

    def run(self):
        result = self.UserProxyAgent.initiate_chat(
            self.StockMarketAssistantAgent,
            message="""What date is today? Compare the year-to-date gain for META and TESLA.""",
            summary_method="reflection_with_llm")