import logging

from telebot_handler import TelebotHandler
from telebot_dispatcher import TelebotDispatcher
from telebot_webhook import TelebotWebhook
from telebot_db import TelebotDB

TOKEN = r'534976981:AAGHLv39JdHzQhjAwEb6QG1YkJ5jNsv4hk4'
WEBHOOK = r'https://44953de7.ngrok.io/'

if __name__ == '__main__':
    logging.basicConfig(filename='debug.log', level=logging.INFO, filemode='w',
                        format='%(asctime)s - %(name)s - %(levelname)s - %(filename)s[LINE:%(lineno)d]\n%(message)s\n')

    bot = TelebotHandler(TOKEN, WEBHOOK)
    db = TelebotDB()

    dispatcher = TelebotDispatcher(bot, db)
    dispatcher.start()

    webhook = TelebotWebhook(bot, db)
    webhook.run()

    dispatcher.stop()
