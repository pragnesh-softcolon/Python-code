# 14) Write a program to understand the order of execution of methods in several base classes according to method resolution order (MRO).

class A:
    def display(self):
        print(" In class A")
class B:
     def display(self):
        print(" In class B")
class C:
    def display(self):
        print(" In class C")
# classes ordering
class X(A,B):
    def __init__(self):
        print("Constructor X")
class Y(B,C):
    def __init__(self):
        print("Constructor Y")
class P(X,Y,C):
    def __init__(self):
        print("Constructor P")
r = P()
 # it prints the lookup order
print(P.__mro__)
print(P.mro())