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

    def add_five(self, x):
        """Bad code because it is not DRY. Repeats same code that could be either done with a loop or simply adding five"""
        x = x + 1
        x = x + 1
        x = x + 1
        x = x + 1
        x = x + 1
        return x

    def display_numbers(self, x, y):
        """Example of YAGNI(You aren't going to need it) since you are inputing the numbers already"""
        print(x)
        print(y)



Calculator = Calculator()