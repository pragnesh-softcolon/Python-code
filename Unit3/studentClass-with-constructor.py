# 2) Write a program to create a Student class with a constructor having more than one parameter.

class Student:
    def __init__(self,name,std,marks):
        self.ename=name
        self.estd=std
        self.emarks=marks
    def display(self):
        print("my name is",self.ename)
s1=Student("vedant",9,80)
s1.display()