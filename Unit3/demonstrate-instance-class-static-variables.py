# 3) Write a program to demonstrate the use of instance and class/static variables.

#to understand instance variable
class sample:
    def __init__(self):
        self.x=10
    def modify(self):
        self.x+=1
        
s1=sample()
s2=sample()
print("x in s1=",s1.x)
print("x in s2=",s2.x)
s1.modify()
print("x in s1=",s1.x)
print("x in s2=",s2.x)