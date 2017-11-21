class InputValue():
    
    def __init__(self, jsonResponse):
        self.coinbase = jsonResponse.get('coinbase')
        self.sequence = jsonResponse["sequence"]
        self.n = jsonResponse["n"]

        if( not self.coinbase):
            self.txid = jsonResponse["txid"]
            self.vout = jsonResponse["vout"]
            self.addr = jsonResponse["addr"]
            self.value = jsonResponse["value"]
            self.value_sat = jsonResponse["valueSat"]
            self.double_spent_ts_id = jsonResponse["doubleSpenxTxID"]
