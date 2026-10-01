# Python program to demonstrate various types of arguments

# Positional arguments
def add(a, b):
    print("Sum:", a + b)

add(10, 20)


# Keyword arguments
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(age=20, name="Rahul")


# Default argument
def greet(name="Student"):
    print("Hello", name)

greet()
greet("Rahul")


# Variable-length arguments
def total(*numbers):
    print("Total:", sum(numbers))

total(10, 20)
total(10, 20, 30, 40)
