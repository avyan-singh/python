class Account:

    def __init__(self,name,balance):
        self.owner=name
        self.balance=balance   

    def Deposit(self,deposit=0):
        self.deposit=deposit
        self.balance+=self.deposit
        return f"Money deposited now you balance is {self.balance}"
    
    def Withdraw(self,withdraw=0):
        self.withdraw=withdraw
        if self.balance>=self.withdraw:
            self.balance-=self.withdraw
            return f"Withdrawed money now your balance is {self.balance}"
        else:
            return 'Not enough balance'

    def __str__(self):
        return f"Account owner:   {self.owner}\nAccount balance: {self.balance}"
       

acct1 = Account('Jose',100)

print(acct1)
print(acct1.owner)
print(acct1.balance)
print(acct1.Deposit(50))
print(acct1.Withdraw(75))
print(acct1.Withdraw(500))
        