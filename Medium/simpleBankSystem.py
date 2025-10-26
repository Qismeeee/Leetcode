class Bank(object):

    def __init__(self, balance):
        self.bal = balance
        self.n = len(balance)

    def _valid(self, acc):
        return 1 <= acc <= self.n

    def transfer(self, account1, account2, money):
        if not self._valid(account1) or not self._valid(account2):
            return False
        if self.bal[account1 - 1] < money:
            return False
        self.bal[account1 - 1] -= money
        self.bal[account2 - 1] += money
        return True

    def deposit(self, account, money):
        if not self._valid(account):
            return False
        self.bal[account - 1] += money
        return True

    def withdraw(self, account, money):
        if not self._valid(account):
            return False
        if self.bal[account - 1] < money:
            return False
        self.bal[account - 1] -= money
        return True

bank = Bank([10, 100, 20, 50, 30])

print(bank.withdraw(3, 10))     # True, account 3: 20 -> 10
print(bank.transfer(5, 1, 20))  # True, account 5: 30->10, account 1:10->30
print(bank.deposit(5, 20))      # True, account 5: 10->30
print(bank.transfer(3, 4, 15))  # False, account 3 only has 10
print(bank.withdraw(10, 50))    # False, account 10 doesn't exist

print(bank.bal)                 # Final balances to inspect
