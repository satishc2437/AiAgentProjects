# This file implements the Stock Market Assistant Agent. This agent is responsible for providing information about the stock market.

# Importing the required libraries
from Agents.Utils import get_config_list
from autogen import AssistantAgent

class StockMarketAssistant:
    __AGENT_NAME = "StockMarketAssistant"
    __MODEL_FILTER = { "tags": ["generic"] }
    __system_message = """Hello! I am the Stock Market Assistant.
    I am here to help you with information about the stock market.
    I can provide you with the latest stock prices, market trends, and investment advice.
    Feel free to ask me any questions related to the stock market."""

    def get_agent(self):
        # Get the list of configurations based on the filter dictionary
        llm_config = get_config_list(self.__MODEL_FILTER)
        llm_config.update({
            "cache_seed": 41,
            "temperature": 0,
        })

        # Instantiate the agent
        return AssistantAgent(
            self.__AGENT_NAME,
            llm_config = llm_config,
            system_message = self.__system_message,
        )

