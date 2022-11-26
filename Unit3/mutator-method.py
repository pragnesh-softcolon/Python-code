# 4) Write a program to store data into instances using mutator methods and to retrieve data from the instances using accessor methods.

class Student:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setMarks(self, marks):
        self.marks = marks

    def getMarks(self):
        return self.marks


n = int(input("how any student?"))
i = 0
while (i < n):
    s = Student()
    name = input("enter name:=")
    s.setName(name)
    marks = input("enter Marks:=")
    s.setMarks(marks)
    print("hi", s.getName())
    print("your marks", s.getMarks())
    i = i + 1
    print("---------------------")

