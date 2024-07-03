# This file implements various utility functions that are used by the agents.

# Path: Agents/Utils.py

# Importing the required libraries
import os
import autogen

# This method retrieves a list of configurations based on a filter dictionary.
# The filter dictionary is used to specify the desired configurations.
# The method uses the autogen library to load the configurations from a JSON file.
# The JSON file is located in the same directory as this script.
# The method returns a dictionary with the list of configurations.
def get_config_list(filter_dict):
    config_list = autogen.config_list_from_json(env_or_file="model_config_list.json", file_location=os.path.dirname(__file__), filter_dict=filter_dict)
    return {"config_list" : config_list}