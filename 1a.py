
#1(A) Create classes for BankAccount, SavingsAccount and
#CheckingAccount and implement methods for deposit,
#withdrawal, balance inquiry and interest calculation 

class BankAccount: 
    def __init__(self, account_number, balance=0): 
        self.account_number = account_number 
        self.balance = balance 
    def deposit(self, amount): 
        self.balance += amount 
        print(f"Deposited ${amount}. New balance: ${self.balance}")  
    def withdraw(self, amount): 
        if self.balance >= amount: 
            self.balance -= amount 
            print(f"Withdrew ${amount}. New balance: ${self.balance}") 
        else: 
            print("Insufficient funds!") 
    def inquiry(self): 
            print(f"Account Balance: ${self.balance}") 
class SavingsAccount(BankAccount): 
    def calculate_interest(self, rate): 
        interest = self.balance * (rate / 100) 
        self.deposit(interest) 
        print(f"Interest of ${interest} added. New balance: ${self.balance}") 
class CheckingAccount(BankAccount): 
    def overdraft_protection(self, amount): 
        if self.balance >= amount: 
            self.balance -= amount 
            print(f"Withdrew ${amount}. New balance: ${self.balance}") 
        else: 
            print("Overdraft Protection: Insufficient funds!") 
            print("Transaction canceled.") 
# Example usage 
savings_acc = SavingsAccount(account_number="SAV12345", balance=1000) 
savings_acc.deposit(500) 
savings_acc.calculate_interest(2)  # 2% interest rate 
savings_acc.inquiry() 
checking_acc = CheckingAccount(account_number="CHK67890", balance=500) 
checking_acc.withdraw(600)  # This will fail due to insufficient funds 
checking_acc.overdraft_protection(600)  # With overdraft protection 
checking_acc.inquiry() 
