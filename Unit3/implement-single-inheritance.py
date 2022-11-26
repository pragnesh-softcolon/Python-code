# 12) Write a program to implement single inheritance in which two subclasses are derived from a single base class.

class Bank(object):
    cash=500000
    @classmethod
    def available_cash(cls):
        print(cls.cash)
        
class AndraBank(Bank):
    pass

class StateBank(Bank):
    cash=200000
    @classmethod
    def available_cash(cls):
        print(cls.cash+Bank.cash)
        
a=AndraBank()
a.available_cash()
s=StateBank()
s.available_cash()