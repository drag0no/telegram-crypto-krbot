import requests
import logging
import json


class CryptoApi:

    def __init__(self):
        self.api_url = r'https://api.coinmarketcap.com/v1/ticker/'

    def get_price(self, crypto_name):
        url = self.api_url + crypto_name
        r = requests.post(url).json()
        logging.info(json.dumps(r, indent=2, ensure_ascii=False))
        price = r[-1]['price_usd']
        return price
