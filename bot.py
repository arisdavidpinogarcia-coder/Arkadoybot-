import os
import requests
from telegram import Update, Bot
from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackContext, Updater

# Load environment variables
API_KEY = os.getenv('API_KEY')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

bot = Bot(token=TELEGRAM_TOKEN)

# Function to get football data
def get_football_data():
    url = f'https://api.football-data.org/v2/matches?apikey={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Command to start the bot
def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hello! I am your football bot. Use /football to get football data.')

# Command to fetch football data
def football(update: Update, context: CallbackContext):
    data = get_football_data()
    if data:
        update.message.reply_text(f'Football Data: {data}')
    else:
        update.message.reply_text('Failed to retrieve data.')

def main():
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    
    # Adding command handlers
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('football', football))

    # Start the Bot
    updater.start_polling()  
    updater.idle()

if __name__ == '__main__':
    main()