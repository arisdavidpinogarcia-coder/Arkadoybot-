import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def main():
    try:
        api_key = os.getenv('API_KEY')
        if not api_key:
            logging.error("API_KEY environment variable not set.")
            return
        # Your bot logic here
        logging.info("Bot is running...")
        # Example: use the api_key for some operation
    except Exception as e:
        logging.exception("An error occurred: %s", e)

if __name__ == '__main__':
    main()