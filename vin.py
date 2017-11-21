from inputValue import InputValue

class Vin():

    def __init__(self, jsonResponse):
        self.inputs = []
        for inp in jsonResponse:
            iv = InputValue(inp)
            self.inputs.append(iv)