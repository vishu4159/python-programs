# Python program to demonstrate method overloading

class Calculator:

    def add(self, a, b, c=0):
        return a + b + c


calculator = Calculator()

print("Addition of two numbers:", calculator.add(10, 20))

print("Addition of three numbers:", calculator.add(10, 20, 30))
