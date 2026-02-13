class Calculator:

    def add_and_sub(self, x, y, addOrSub):
        """Bad code because it does not follow the idea of single responsibility."""
        if(addOrSub == "add"):
            return x + y
        elif(addOrSub == "sub"):
            return x - y



    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y

    def square(self, x):
        return x ** 2


Calculator = Calculator()