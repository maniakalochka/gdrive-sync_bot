from bot import bot
from commands_text import *
from db.db_manager import *
import mimetypes

user_states = {}

STATE_START = 0

def handle_document(message):
    return message.document.file_id, message.document.file_name, message.document.file_size

def handle_photo(message):
    file_info = bot.get_file(message.photo[-1].file_id)
    file_size = file_info.file_size
    return message.photo[-1].file_id, 'photo.jpg', file_size

def handle_audio(message):
    return message.audio.file_id, message.audio.title, message.audio.file_size

def handle_video(message):
    return message.video.file_id, message.video.file_name, message.video.file_size

handlers = {
    'document': handle_document,
    'photo': handle_photo,
    'audio': handle_audio,
    'video': handle_video,
}

@bot.message_handler(content_types=['document', 'photo', 'audio', 'video'])
def process_upload_step(message):
    chat_id = message.chat.id
    if message.text == '/cancel':
        user_states[chat_id] = STATE_START
        bot.send_message(chat_id, CANCEL_MSG)
    if message.content_type in handlers:
        file_id, name, file_size = handlers[message.content_type](message)
        mimetype, _ = mimetypes.guess_type(name)
        bot.reply_to(message, UPLOAD_OK)
        upload_file(file_id, name, mimetype, file_size)
    else: 
        bot.reply_to(message, UPLOAD_WRONG_FORMAT)

       
def process_show_dirs_and_files_step(message):
    chat_id = message.chat.id
    if message.text == '/cancel':
        user_states[chat_id] = STATE_START
        bot.send_message(chat_id, CANCEL_MSG)
    else:
        
        res = show_current_dir_elem()
        res = '\n'.join(res)
        bot.send_message(chat_id, res)






