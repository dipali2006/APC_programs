# transaction.py

def deposit(balance, amount):
    balance = balance + amount
    return balance

def withdraw(balance, amount):
    if amount <= balance:
        balance = balance - amount
        return balance
    else:
        print("Insufficient Balance")
        return balance
