# 13) Write a program to implement multiple inheritances using two base classes.

class Father:
    def height(self):
        print("height is 6.0 foot")
        
class Mother:
    def color(self):
        print("color is pink")
        
class Child(Father,Mother):
    pass

c=Child()
print("child's inherited qualities:")
c.height()
c.color()