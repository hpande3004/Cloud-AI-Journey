class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

account = BankAccount(5000)
print(account.balance)              # Output: 5000


class BankAccount:

    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self._balance = amount
        else:
            print("Balance cannot be negative")

account = BankAccount(5000)

print(account.balance)

account.balance = 10000

print(account.balance)

account.balance = -500