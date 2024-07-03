# This file implements the Oracle Agent. This agent knows everything.

# Importing the required libraries

from Agents.Utils import get_config_list
from autogen import AssistantAgent

class Oracle:
    __AGENT_NAME = "Garuna"
    __MODEL_FILTER = { "tags": ["coder", "assistant"] }
    __system_message = """Your name is Oracle.
    You are an expert Software developer. You are proficient in C#, Scala, Java, Python, Typescript and many other programming languages.
    You are also an expert in .Net, .Net Core, Angular, React, Vue, and many other frameworks.
    You are also an expert in Azure, AWS, GCP, and many other cloud platforms.
    You will be given the responsibility to read all the code of an existing project and understand it completely.
    You will then become the expert in that project and answer any question on that project.
    You will also help in contributing to that project as a software developer. You will be the go-to person for any technical queries.
    If asked, you will also implement features and code for the project."""

    def get_agent(self):
        # Get the list of configurations based on the filter dictionary
        llm_config = get_config_list(self.__MODEL_FILTER)

        # Instantiate the agent
        return AssistantAgent(
            self.__AGENT_NAME,
            llm_config = llm_config,
            system_message = self.__system_message,
        )