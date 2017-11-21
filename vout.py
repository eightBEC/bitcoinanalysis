from outputValue import OutputValue

class Vout():

    def __init__(self, jsonResponse):
        self.outputs = []
        for outp in jsonResponse:
            ov = OutputValue(outp)
            self.outputs.append(ov)