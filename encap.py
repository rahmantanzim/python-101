class BankAccount:
    def __init__(self, balance):
        self._balance = balance
        
    def deposite(self, amount):
        self._balance += amount
    
    def getbalance(self):
        return self._balance
    
my_account = BankAccount(10000)
my_account.deposite(2000)

print(my_account._balance)