# 1) Write a program to create a Student class with name, age, and marks as data members. Also, create a method named display() to view the student details. Create an object for the Student class and call the method using the object.

class Student:
    def __init__(self):
        self.name="sumit"
        self.age=50
        self.marks=88
    def display(self):
        print("my name is",self.name)
        print("my age is",self.age)
        print("my marks are",self.marks)
s1=Student()
s1.display()