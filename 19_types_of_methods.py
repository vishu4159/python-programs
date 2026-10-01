# Python program to demonstrate various types of methods

class Student:

    school = "ABC School"

    # Instance method
    def display(self):
        print("This is an instance method.")

    # Class method
    @classmethod
    def show_school(cls):
        print("School:", cls.school)

    # Static method
    @staticmethod
    def welcome():
        print("Welcome to Python programming.")


student = Student()

# Calling instance method
student.display()

# Calling class method
Student.show_school()

# Calling static method
Student.welcome()
