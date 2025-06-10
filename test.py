# test.py
from function_app_git import willrain
import logging
from datetime import datetime

logging.basicConfig(filename="willrain.log", level=logging.INFO)

if __name__ == "__main__":
    """
    Checks the weather forecast and logs the result.
    """
    try:
        logging.info(datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S"))
        logging.info("Starting weather check...")
        willrain()
        logging.info("Weather check completed successfully.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

