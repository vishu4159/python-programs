# Python program to demonstrate various forms of inheritance

# 1. Single Inheritance
class Animal:
    def eat(self):
        print("Animal eats food.")


class Dog(Animal):
    def bark(self):
        print("Dog barks.")


dog = Dog()
print("Single Inheritance:")
dog.eat()
dog.bark()


# 2. Multiple Inheritance
class Father:
    def father_property(self):
        print("Father's property")


class Mother:
    def mother_property(self):
        print("Mother's property")


class Child(Father, Mother):
    def child_property(self):
        print("Child's property")


child = Child()
print("\nMultiple Inheritance:")
child.father_property()
child.mother_property()
child.child_property()


# 3. Multilevel Inheritance
class Grandparent:
    def grandparent_property(self):
        print("Grandparent's property")


class Parent(Grandparent):
    def parent_property(self):
        print("Parent's property")


class Son(Parent):
    def son_property(self):
        print("Son's property")


son = Son()
print("\nMultilevel Inheritance:")
son.grandparent_property()
son.parent_property()
son.son_property()


# 4. Hierarchical Inheritance
class Vehicle:
    def start(self):
        print("Vehicle starts.")


class Car(Vehicle):
    def drive(self):
        print("Car is driving.")


class Bike(Vehicle):
    def ride(self):
        print("Bike is riding.")


car = Car()
bike = Bike()

print("\nHierarchical Inheritance:")
car.start()
car.drive()
bike.start()
bike.ride()
