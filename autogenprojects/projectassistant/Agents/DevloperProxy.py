# This class implements the Developer Proxy Agent

# Importing the required libraries
from autogen import UserProxyAgent
from autogen.coding import LocalCommandLineCodeExecutor

class DeveloperProxy:
    __AGENT_NAME = "Bot"
    __System_Message = "Hello, I am the Developer Proxy Agent. I will help you with your queries. Type 'exit' to end the conversation."
    __TERMINATION_MESSAGE = "exit"

    def get_agent(self):
        return UserProxyAgent(
            self.__AGENT_NAME,
            system_message=self.__System_Message,
            human_input_mode="TERMINATE",
            max_consecutive_auto_reply=10,
            is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
            code_execution_config={
                    # the executor to run the generated code
                    "executor": LocalCommandLineCodeExecutor(work_dir="coding"),
                }
            )


