#a calculator app
from modes.baseMode import Mode


class Calculator(Mode):
    prompt = "calc mode"
    name = "calc"
    def __init__(self):
        self.prompt = "calc mode"
        self.name="calc"
    def handleInput(self, i, modes):
        if i == "1+1":
            print("2")
            return Calculator
        else:
            return self.defaultInput(i, modes)
    def init(self):
        print("the calculator is good for simple calculations")