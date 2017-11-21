class OutputValue():
    
    def __init__(self, jsonResponse):
        (addresses, typ, hex_repr)= self.parseScriptPubKey(jsonResponse["scriptPubKey"])
        self.addresses = addresses
        self.typ = typ
        self.hex_repr = hex_repr
        self.n = jsonResponse["n"]
        self.value = jsonResponse["value"]
        self.double_spent_ts_id = jsonResponse.get("doubleSpenxTxID")

    def parseScriptPubKey(self,scriptPubKeyDict):
        addresses = scriptPubKeyDict["addresses"]
        typ = scriptPubKeyDict["type"]
        hex_repr = scriptPubKeyDict["hex"]
        return (addresses, typ, hex_repr)