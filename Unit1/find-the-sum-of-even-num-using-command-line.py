# Write a python program to find the sum of even numbers using command line arguments.

# first way to take user

# import sys
# n=int(sys.argv[1])
# i=2
# sum=0

# while(i<=n):
#     sum=sum+i
#     i=i+2
# print("sum of even number=", sum)

#second way to take user input

n = int(input("Enter value of n:= "))
i=2
sum=0
while(i<=n) :
    sum=sum+i
    i=i+2
print("Sum of even number=", sum)