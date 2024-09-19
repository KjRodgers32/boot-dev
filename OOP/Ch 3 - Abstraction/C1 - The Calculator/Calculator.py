class Calculator:
    def __init__(self):
        self.__result = 0
    
    def add(self, x):
        self.__result += x
    
    def subtract(self, x):
        self.__result -= x
    
    def multiply(self, x):
        self.__result *= x
    
    def divide(self, x):
        if x == 0:
            self.__raise_if_divde_by_zero()
        self.__result /= x
    
    def modulo(self, x):
        if x == 0:
            self.__raise_if_divde_by_zero()
        self.__result %= x
    
    def power(self, x):
        self.__result **= x
    
    def square_root(self):
       self.__result **= .5
    
    def clear(self):
        self.__result = 0
    
    def get_result(self):
        return self.__result

    def __raise_if_divde_by_zero(self):
        raise ValueError("Cannot divide by zero")