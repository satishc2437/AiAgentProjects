# This is the main file. The project execution starts from here.

# Importing the required libraries
from ScenarioManager import ScenarioManager

def main():
    # Instantiate the chat
    ScenarioManager().start_scenario("stock_market_analysis")

if __name__ == "__main__":
    main()
