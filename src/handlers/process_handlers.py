from email.policy import default
from bot import bot
from commands_text import *
from db.db_manager import *
import mimetypes

user_states = {}

STATE_START = 0

@bot.message_handler(content_types=['document'])
def process_upload_step(message):
    '''Шаг процесса загрузки файла: команда /upload'''
    chat_id = message.chat.id
    if message.text == '/cancel':
        user_states[chat_id] = STATE_START
        bot.send_message(chat_id, CANCEL_MSG)
    else:
        while True:
            chat_id = message.chat.id
            document = message.document
            if not document:
                raise Exception('Это не документ. Повторите попытку:')
            
            name = document.file_name
            mimetype, _ = mimetypes.guess_type(name)
            file_size = document.file_size
            bot.reply_to(message, UPLOAD_OK)
            tg_file_id = message.document.file_id
            default_name = message.document.file_name

            upload_file(tg_file_id, default_name, mimetype, file_size)
            break
