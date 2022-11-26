# 16) Write a program to overload the addition operator (+) to make it act on the class objects.

class Book_A:
    def __init__(self, pages):
        self.pages = pages

    def __str__(self):
        return "{0}".format(self.pages)
    def __add__(self, other):
        pages = self.pages + other.pages
        return Book_A(pages)

class Book_B:
     def __init__(self, pages):
        self.pages = pages

p1 = Book_A(100)
p2 = Book_B(100)
print("total pages:=",p1+p2)