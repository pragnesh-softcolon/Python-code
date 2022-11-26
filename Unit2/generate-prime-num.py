# Write a program to generate prime numbers with the help of a function to test prime or not.

def primeex(lr,ur):
    for num in range(lr,ur+1):
        if num>1:
            for i in range(2,num):
                if(num%i)==0:
                    break
                else:
                    print(num)

lr=int(input("enter lower range:="))
ur=int(input("enter upper range:="))
primeex(lr,ur)