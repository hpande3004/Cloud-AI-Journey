'''Mini Project 2
Bank Account System'''

class BankAccount:
    def __init__(self, accountHolder, balance):
        self.accountHolder = accountHolder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("₹",amount,"deposited successfully")

        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")

        elif amount > self.balance:
            print("Insufficient Balance")

        else:
            self.balance -= amount 
            print("₹",amount,"withdrawn successfully")

    def show_balance(self):
        print("Account Holder: ", self.accountHolder)
        print("Balance: ₹", self.balance)

class SavingAccount(BankAccount):
    def withdraw(self, amount):
        if amount > self.balance:
            print("Savings Account: Insufficient Balance")
        else:
            self.balance -= amount
            print("₹",amount,"withdrawn from Savings Account")

class CurrentAccount(BankAccount):

    def withdraw(self, amount):
        if amount > self.balance + 10000:
            print("Current Account withdrawl limit exceeds!")
        else:
            self.balance -= amount 
            print("₹",amount,"withdrawn from current account")

savings = SavingAccount("Rahul", 20000)
current = CurrentAccount("Suresh", 50000)
print("\n =====Saving Account=====")
savings.show_balance()
savings.deposit(5000)
savings.withdraw(3000)
savings.show_balance()

print("\n =====Current Account=====")
current.show_balance()
current.withdraw(55000)
current.show_balance()