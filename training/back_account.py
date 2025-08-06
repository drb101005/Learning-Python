# 2. BankAccount class
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount

account = BankAccount(1000)
try:
    account.withdraw(1500)
except ValueError as e:
    print(e)
