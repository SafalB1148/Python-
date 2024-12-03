class Account:
    def __init__(self,accNo,name,balance,accType):
        self.accNo = accNo
        self.name = name
        self.balance = balance
        self.accType = accType
    def getbalance(self):
        return self.balance
    def withdraw(self,amount):
        if self.getbalance() <=amount:
            return False
        self.balance-=amount
        return True
    def deposit(self,amount):
        self.balance+=amount
    def printAccDetails(self):
        print(f"AccNo: {self.accNo},Name: {self.name},Balance: {self.balance},accType: {self.accType}")
a1=Account(50,"safal",100000,"Saving")
a2=Account(111,"Dipsikha",80000,"saving")
a1.withdraw(10000)
a1.deposit(20000)
a1.printAccDetails()
a2.withdraw(500)
a2.deposit(1500)
a2.printAccDetails()

if(not a1.withdraw(200000)):
    print("Withdraw amount is more than the balance.so cant withdraw.")



