# Write a program to search an element in the list using for loop and also demonstrate the use of “else” with for loop.

n = [6, 5, 3, 8, 4, 2, 5, 4, 11]
num=int(input("enter number for search element: ") )
flag = False

for i in n:
    if(i == num) :
        flag = True
        break
    else:
        flag = False

if(flag):
    print ("Element Exists",num)
else :
    print ("Element not Exists",num)