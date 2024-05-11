from bot import bot, ADMIN_TG_ID
from commands_text import *

command_list = [
    'start', 'help',
]


@bot.message_handler(commands=['start'], func=lambda message: message.from_user.id == ADMIN_TG_ID)
def start_cmd(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, START_CMD_SUCCESS)
    bot.send_message(chat_id, START_CMD_CONTINUE)
    
