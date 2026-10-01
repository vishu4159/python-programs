# Python program to demonstrate the use of methods

class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


calculator = Calculator()

print("Addition:", calculator.add(10, 5))
print("Subtraction:", calculator.subtract(10, 5))
