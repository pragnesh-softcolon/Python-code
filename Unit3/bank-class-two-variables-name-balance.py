# 7) Create a Bank class with two variables name and balance. Implement a constructor to initialize the variables. Also, implement deposit and withdrawals using instance methods.

import sys
class Bank:
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        return self.balance
    def withdraw(self,amount):
        if amount < self.balance:
            print("balance amount is lessthen so no withdrawal")
        else:
            self.balance-=amount
            return self.balance
name=input("enter name :- ")
b=Bank(name)

while(True):
    print("d-deposit,w-withdraw,e-exit")
    choice=input("your choice:- ")
    if choice=='e' or choice=='E':
        sys.exit()
        amt=float(input("enter amount :-  "))
    if choice=='d' or choice=='D':
        print("balance after deposit",b.deposit(amt))
    elif choice=='w' or choice=='W':
        print("balance after deposit",b.withdraw(amt))
        