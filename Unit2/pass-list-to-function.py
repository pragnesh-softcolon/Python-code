# Write a program to pass a list to a function and display it.

def displayList(a):
    print("List is:",a)

def createList(a,j):
    a.append(j)

a=[]
n=int(input("enter how many elements u want:="))
for i in range(n):
    createList(a,int(input("enter element:=")))
    displayList(a)