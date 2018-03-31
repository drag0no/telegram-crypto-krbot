import logging
import json

from flask import Flask, request, jsonify

from crypto_dictionary import crypto_dictionary
from crypto_api import CryptoApi


class TelebotWebhook:

    def __init__(self, bot_handler, db):
        self.token = bot_handler.get_token()
        self.bot = bot_handler
        self.db = db
        self.crypto_api = CryptoApi()
        self.flsk = Flask(__name__)
        self.flsk.add_url_rule('/', 'index_page', self.index_page)
        self.flsk.add_url_rule('/' + self.token, 'webhook_page', self.webhook_page, methods=['POST', 'GET'])

    def run(self):
        self.flsk.run()

    def index_page(self):
        return '<h1>Telegram CryptoKrBot Welcome Page</h1>'

    def webhook_page(self):
        if request.method == 'POST':
            r = request.get_json()
            logging.info(json.dumps(r, indent=2, ensure_ascii=False))
            chat_id = r['message']['chat']['id']
            message_id = r['message']['message_id']
            message_text = r['message']['text']
            message_text = message_text.lower()

            if '/start' in message_text:
                self.db.insert_chatid(chat_id)
            elif '/stop' in message_text:
                self.db.delete_chatid(chat_id)
            else:
                for key, value in crypto_dictionary.items():
                    if key in message_text:
                        price = self.crypto_api.get_price(value)
                        send_message = key + ":\t" + price
                        self.bot.send_message(chat_id, send_message, message_id)
            return jsonify(r)
        return '<h1>Telegram CryptoKrBot WebHook Page</h1>'
