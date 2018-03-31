from multiprocessing import Process
from time import sleep

from crypto_dictionary import crypto_dictionary
from crypto_api import CryptoApi


class TelebotDispatcher:

    def __init__(self, bot_handler, db):
        self.bot = bot_handler
        self.db = db
        self.crypto_api = CryptoApi()
        self.run_flag = False
        self.process = None

    def run(self):
        while self.run_flag:
            chatid_list = self.db.get_chatids()
            if chatid_list:
                text = ''
                for key, value in crypto_dictionary.items():
                    price = self.crypto_api.get_price(value)
                    text += '{}:\t{}\n'.format(key, price)
                for chat_id in chatid_list:
                    self.bot.send_message(chat_id, text)
            sleep(60)

    def start(self):
        if self.run_flag:
            self.stop()
        self.process = Process(target=self.run)
        self.run_flag = True
        self.process.start()

    def stop(self):
        self.run_flag = False
        self.process.join()
