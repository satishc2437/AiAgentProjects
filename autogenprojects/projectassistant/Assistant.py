# This file implements the entry class for Assistant

# Importing the required libraries
from Agents.AgentManager import AgentManager

class Assistant:
    def __init__(self):
        pass

    def start_chat(self):
        agentManager = AgentManager()
        dev_proxy_agent = agentManager.get_dev_proxy_agent()
        oracle_agent = agentManager.get_oracle_agent()

        if dev_proxy_agent is None or oracle_agent is None:
            raise ValueError("Agent not found")

        # start the chat between agents
        result = dev_proxy_agent.initiate_chat(oracle_agent)

    def run(self):
        self.start_chat()