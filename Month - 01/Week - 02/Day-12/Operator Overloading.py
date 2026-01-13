'''
12.9 - Operator Overloading
Goal: Allow adding two wallets: w1 w2. 
Deep Dive: Define_add. When Python sees, it calls this method. 
This allows objects to behave like native types (Polymor-phism).
'''

class Wallet:
    def __init__(self, balance):
        self.balance = balance

    def __add__(self, other):
        if isinstance(other, Wallet):
            return Wallet(self.balance + other.balance)
        return NotImplemented

    def __str__(self):
        return f"Wallet balance: {self.balance}"

w1 = Wallet(100)
w2 = Wallet(250)
w3 = w1 + w2
print(w3) 
