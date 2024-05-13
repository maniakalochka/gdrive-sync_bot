from bot import bot, ADMIN_TG_ID
from commands_text import *
from utils.utils import admin_required
from handlers.process_handlers import *

command_list = [
    'start', 'help',
    ''
]


@bot.message_handler(commands=['start'])
@admin_required
def start_cmd(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, START_MSG_SUCCESS)
    bot.send_message(chat_id, START_MSG_CONTINUE)


@bot.message_handler(commands=['help'])
@admin_required
def help_cmd(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, HELP_MSG)


@bot.message_handler(commands=['upload'])
@admin_required
def upload_cmd(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, UPLOAD_MSG)
    bot.register_next_step_handler(msg, process_upload_step)
