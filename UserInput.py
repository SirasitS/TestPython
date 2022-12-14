class TextInput:
    def __init__(self):
        self.textResult = ""

    def add(self, character):
        self.textResult += character

    def get_value(self):
        return self.textResult
  

class NumericInput(TextInput):
    def add(self, character):
        if character.isnumeric():
            self.textResult += character
        return self.textResult        


if __name__ == '__main__':
    input = NumericInput()
    input.add("1")
    input.add("a")
    input.add("0")
    print(input.get_value())