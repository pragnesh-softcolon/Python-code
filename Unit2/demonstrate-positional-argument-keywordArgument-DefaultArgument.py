# Write a program to demonstrate the use of positional argument, keyword argument, and default argument.

def concat_str(str1,str2):
    print("concatenate two strings:",str1+str2)

def wish(name,msg="good morning"):
    print("hello",name,"",msg)

def item(name,price):
    print("name of item is:",name,"price of item is:",price)

fname="sumit"
lname="patel"
concat_str(fname,lname)

wish("sumit")
wish("sumit","how r u?")

item("BMW",9900000)
item(price=4500,name="node mcu")