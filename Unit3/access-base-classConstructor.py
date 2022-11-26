# 10) Write a program to access the base class constructor from a subclass by using the super() method and also without using the super() method.

# WITHOUT SUPER():

class Parent:
 # create a parent class method
    def show(self):
        print("Inside Parent class")
 # create a child class
class Child(Parent):
 # Create a child class method
    def display(self):
        print("Inside Child class")

obj = Child()
obj.display()
# Calling Parent class
obj.show()

# USING SUPER():

# [python]
class Parent():
    def show(self):
        print("Inside Parent")

class Child(Parent):
    def show(self):
 # Calling the parent's class
 # method
        super().show()
        print("Inside Child")

# Driver's code
obj = Child()
obj.show()
