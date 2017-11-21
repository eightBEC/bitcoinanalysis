import requests
import json
from transaction import Transaction

class BitcoinHistory():

    def __init__(self):
        self.host = 'https://blockexplorer.com'
        pass

    def getBlockRange(self, start_inclusive, end_exclusive):
        block_hashes = []
        url_route = '/api/block-index/'
        for block_id in range(start_inclusive,end_exclusive):
            curr_url_route =url_route + str(block_id)
            result = self._callApi(curr_url_route)
            block_hashes.append(result["blockHash"])
        return block_hashes

    def getTransactionsByBlockHash(self, block_hash):
        transactions = []
        url_route = '/api/txs/?block=' + str(block_hash)
        result = self._callApi(url_route)
        print(result["pagesTotal"])
        for single_tx in result["txs"]:
            tx = Transaction(single_tx)    
            transactions.append(tx)
        return transactions

    def _callApi(self, url_route):
        url_to_get = self.host + url_route
        r = requests.get(url_to_get)
        if(r.status_code == 200):
            return r.json()
        else:
            print(r.text)
            return {}


bh = BitcoinHistory()
txs = bh.getTransactionsByBlockHash(bh.getBlockRange(32100,32103)[0])
