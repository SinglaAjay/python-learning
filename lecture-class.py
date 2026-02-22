class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def credit(self, amount):
        """Add money to the account"""
        if amount > 0:
            self.balance += amount
            print(f"Credited: ${amount}. New balance: ${self.balance}")
        else:
            print("Credit amount must be positive")
    
    def debit(self, amount):
        """Withdraw money from the account"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Debited: ${amount}. New balance: ${self.balance}")
        elif amount > self.balance:
            print("Insufficient funds")
        else:
            print("Debit amount must be positive")

creditAmt= float(input("Enter the amount to credit: "))

bnkObj = BankAccount("123456789", 0)
bnkObj.credit(creditAmt)

debitAmt= float(input("Enter the amount to debit: "))
bnkObj.debit(debitAmt)