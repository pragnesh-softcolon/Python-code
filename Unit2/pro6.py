ans = 0
num = int(input("Enter Number to check prime or not: "))
for i in range(1, num+1):
    if (num % i) == 0:
        ans = ans+1
    if (ans == 2):
        print("no is prime")
    else:
        print("no is not prime")
