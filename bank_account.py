class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Depsited {amount} New Balance: {self.balance}"
        else:
            return "Invalid deposit amount"

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance-1000:
            self.balance -= amount
            return f"Withdrawn {amount} New balance: {self.balance}"
        else:
            return "Insufficient balance"

    def check_balance(self):
        return f"Your current balance is: {self.balance}"




