# 15) Write a program to check the object type to know whether the method exists in the object or not.

class Dog:
    def bark(self):
        print("Bow,Wow!")
class Duck:
    def Talk(self):
        print("Quack,quack")
class Human:
    def Talk(self):
        print("hello, hi")
def call_talk(obj):
    if hasattr(obj,"talk"):
        obj.Talk()
    elif hasattr(obj,"bark"):
        obj.bark()
    else:
        print("wrong object passed....")

x=Duck()
call_talk(x)

x=Human()
call_talk(x)

x=Dog()
call_talk(x)

