from bot import bot, ADMIN_TG_ID
from commands_text import *


def admin_required(func):  # /TODO переименовать в check_if_user_has_access
    def wrapper(message):
        if message.from_user.id == ADMIN_TG_ID:
            return func(message)
        else:
            bot.send_message(message.chat.id, PERMISSION_DENIED_MSG)
    return wrapper