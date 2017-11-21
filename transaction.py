from vin import Vin
from vout import Vout

class Transaction():

    def __init__(self, jsonResponse):
        print(jsonResponse)
        self.txid = jsonResponse["txid"]
        self.version = jsonResponse["locktime"]
        self.blockhash = jsonResponse["blockhash"]
        self.blockheight = jsonResponse["blockheight"]
        self.confirmations = jsonResponse["confirmations"]
        self.time = jsonResponse["time"]
        self.blocktime = jsonResponse["blocktime"]
        self.value_out = jsonResponse["valueOut"]
        self.size = jsonResponse["size"]
        self.is_coin_base = jsonResponse["isCoinBase"]
        if( not self.is_coin_base ):
            self.value_in = jsonResponse["valueIn"]
            self.fees = jsonResponse["fees"]
        self.vin = Vin(jsonResponse["vin"])
        self.vout = Vout(jsonResponse["vout"])