# Create a program to display memory locations of two variables using id() function, 
# and then use identity operators two compare whether two objects are same or not.
a = 10
b = 101
print("Memory location of a:",id(a))
print("Memory location of b:",id(b))

if(a is b):
    print("a and b have same identity")
else:
    print("a and b do not have same identity")

if(id(a) == id(b)):
    print("a and b have same location")
else:
    print("a and b do not have same location")