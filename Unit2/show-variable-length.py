# Write a program to show variable length argument and its use

def add(n,*n1):
    sum=0
    for i in n1:
        sum=sum+int(i)
        print("addition of numbers is:=",n+sum)

add(1,2)
add(1,2,3)
add(1,2,3,4,5,6,7)