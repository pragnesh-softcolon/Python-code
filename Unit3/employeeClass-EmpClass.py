# 8) Write a program to create an Employee class and make all the members of the Emp class available to another class (My class). [By passing members of one class to another].

class Emp(object):

 # Constructor
    def __init__(self, name):
        self.name = name

 # To get name
    def getName(self):
        return self.name

 # To check if this person is an employee
    def isEmployee(self):
        return False

# Inherited or Subclass (Note Person in bracket)
class MyClass(Emp):

 # Here we return true
    def isEmployee(self):
        return True

# Driver code
e1 = Emp("sumit") # An Object of Person
print(e1.getName(), e1.isEmployee())
m1 = MyClass("bca 5") # An Object of Employee
print(m1.getName(), m1.isEmployee())
