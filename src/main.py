from handlers.handlers import *
from bot import bot
from logger import logger

if __name__ == "__main__":
    logger.info('Бот запустился')
    bot.polling(none_stop=True)