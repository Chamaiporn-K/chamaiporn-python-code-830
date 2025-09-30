class BankAccount:
    def __init__(self,accoutNumer = int,name = str,balance = float):
        self.accoutNumer = accoutNumer
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            return print("Deposit amount must be positive")
        
    def Withdrawal(self,amount):
         if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return print(f"Withdrew ${amount}. New balance: ${self.balance}")
         elif amount > self.balance:
            return print("Insufficient funds")
         else :
            return print("Withdrawal amount must be positive")
    
    def bankFees(self):
        fee = self.balance*0.05
        self.balance -= fee
        return print(f"Bank fees : ${fee} New balance: ${self.balance}")
    
    def display(self):
        return print(f"Accout Number : {self.accoutNumer}\nName : {self.name}\nBalance : {self.balance}")

account = BankAccount("12345",'chamaiporn konglae',10000)
account.deposit(500)
account.Withdrawal(200)
account.bankFees()
account.display()