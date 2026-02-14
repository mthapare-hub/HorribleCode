class Calculator:

    """Good code because it follows the idea of single responsibility."""
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y
    


    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        return x / y

    def square(self, x):
        return x ** 2
    
    def add_five(self, x):
        """This code is DRY because it was not repeating the same code"""
        return x + 5
    

    
Calculator = Calculator()