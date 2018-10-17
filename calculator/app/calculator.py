import time

class Calculator(object):

    def validate_input(self, x, y):
        number_types = (int, float)
        return isinstance(x, number_types) and isinstance(y, number_types)

    def add(self, x, y):
    # validate x and y are numbers
    # add x and y and return the result to the user
        if self.validate_input(x, y): 
            time.sleep(10) # long running process
            return x + y
        else: raise ValueError

    def subtract(self, x, y):
    # validate x and y are numbers
    # subtract y from x and return the result to the user
        pass

    def divide(self, x, y):
    # validate x and y are numbers
    # divide x by y and return the quotient to the user
        if self.validate_input(x, y): return round((x / y) ,2)
        else: raise ValueError

    def multiply(self, x, y):
    # validate x and y are numbers
    # multiply x and y and return the result to the user
        pass