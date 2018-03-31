import json
import logging

import requests


class TelebotHandler:

    def __init__(self, token, webhook_adress):
        self.token = token
        self.api_url = 'https://api.telegram.org/bot{}/'.format(self.token)
        self.del_webhook()
        self.set_webhook(webhook_adress)

    def del_webhook(self):
        r = requests.post(self.api_url + 'deleteWebhook').json()
        logging.info(json.dumps(r, indent=2, ensure_ascii=False))
        return r

    def set_webhook(self, address):
        params = {'url': address + self.token}
        r = requests.post(self.api_url + 'setWebhook', data=params).json()
        logging.info(json.dumps(r, indent=2, ensure_ascii=False))
        return r

    def send_message(self, chat_id, text, reply_mess_id=None):
        params = {'chat_id': chat_id, 'text': text, 'reply_to_message_id': reply_mess_id}
        r = requests.post(self.api_url + 'sendMessage', data=params).json()
        logging.info(json.dumps(r, indent=2, ensure_ascii=False))
        return r

    def get_token(self):
        return self.token
