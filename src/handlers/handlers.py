from bot import bot, ADMIN_TG_ID
from commands_text import *
from utils.utils import admin_required
from handlers.process_handlers import *
from google_api.drive_manager import load_files_from_gdrive
from google_api.drive import service


command_list = [
    '/start', '/help',
    '/upload',
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



@bot.message_handler(commands=['ls'])
@admin_required
def list_files_and_dirs(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, LS)
    bot.register_next_step_handler(msg, process_show_dirs_and_files_step)

@bot.message_handler(commands=['indx'])
@admin_required
def indexing_gdrive(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, INDX)
    load_files_from_gdrive(service)
    bot.send_message(chat_id, INDX_OK)



@bot.message_handler(func=lambda message: True)
@admin_required
def unknown_cmd(message):
    bot.reply_to(message, UNKNOWN)


