import telebot
from dotenv import load_dotenv
import os

# from google_api.drive import CLIENT_SECRETS

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

#--------ADMIN_SECTION-------#

ADMIN_TG_ID = os.getenv('ADMIN_TG_ID')
ADMIN_TG_ID = int(ADMIN_TG_ID)



