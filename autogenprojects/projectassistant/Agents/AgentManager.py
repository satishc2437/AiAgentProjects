# This class implement a Manager that owns creating and managing agents.

# Path: Agents/AgentManager.py

# Importing the required libraries
from numpy import mat
from Agents.DevloperProxy import DeveloperProxy
from Agents.Oracle import Oracle
from Agents.StockMarketAssistant import StockMarketAssistant

class AgentManager:
    def __init__(self):
        self.agents = {}
    
    def get_dev_proxy_agent(self):
        return self.get_agent("dev_proxy")

    def get_oracle_agent(self):
        return self.get_agent("oracle")
    
    def get_agent(self, agent_name):
        if (agent_name not in self.agents):
            match agent_name:
                case "dev_proxy":
                    self.agents[agent_name] = DeveloperProxy().get_agent()
                case "oracle":
                    self.agents[agent_name] = Oracle().get_agent()
                case "stock_market_assistant":
                    self.agents[agent_name] = StockMarketAssistant().get_agent()
                case _:
                    raise ValueError(f"Agent {agent_name} not found")
        return self.agents[agent_name]