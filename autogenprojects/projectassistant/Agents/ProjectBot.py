# ChatAssistant - This will be the front face of the chatbot. It will be responsible for handling the user input and providing the output to the user.
# It will also be responsible for handling the conversation flow.

# Importing the required libraries
import os
import autogen

from Agents.Utils import get_config_list
from autogen import ConversableAgent

class ProjectBot:
    __AGENT_NAME = "Satish"
    __MODEL_FILTER = { "tags": ["conversational"] }
    __system_message = """You are the Project Bot Agent. The User will interact with you directly. The User will provide you inputs. This input you will have to relay to the Engine Agent. You will get the response from Engine Agent and relay it back to the User with appropriate formatting."""

    def __init__(self):
        # Get the list of configurations based on the filter dictionary
        self.llm_config = get_config_list(self.__MODEL_FILTER)

        # Instantiate the agent
        self.agent = ConversableAgent(
            self.__AGENT_NAME,
            llm_config = self.llm_config,
            system_message = self.__system_message,
            code_execution_config=False,
            function_map=None,
            is_termination_msg=lambda msg: msg == "exit",
            human_input_mode="Always"
        )

    def start_chat(self, user_input):
        # Get the response from the agent
        response = self.agent.generate_reply(messages=[{"content": user_input, "role": "User"}])
        return response


