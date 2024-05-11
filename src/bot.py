import telebot
from dotenv import load_dotenv
import os

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

#--------ADMIN_SECTION-------#

ADMIN_TG_ID = os.getenv('ADMIN_TG_ID')