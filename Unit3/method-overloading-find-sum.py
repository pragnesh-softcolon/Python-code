# 17) Write a program to show method overloading to find the sum of two or three numbers.

class Addition:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("sum of three",a+b+c)
        elif a!=None and b!=None:
            print("sum of two",a+b)
        else:
            print("please enter two or three argument")

a=Addition()

a.sum(10,15,20)
a.sum(10.5,20.5)
a.sum(10)