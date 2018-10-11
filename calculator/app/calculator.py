class Calculator(object):

    def validate_input(self, x, y):
        number_types = (int, long, float, complex)
        return isinstance(x, number_types) and isinstance(y, number_types)

    def add(self, x, y):
    # validate x and y are numbers
    # add x and y and return the result to the user
        pass

    def subtract(self, x, y):
    # validate x and y are numbers
    # subtract y from x and return the result to the user
        pass

    def divide(self, x, y):
    # validate x and y are numbers
    # divide x by y and return the quotient to the user
        pass

    def multiply(self, x, y):
    # validate x and y are numbers
    # multiply x and y and return the result to the user
        pass