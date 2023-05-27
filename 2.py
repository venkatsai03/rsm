class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} into Account {self.account_number}. New balance: {self.balance}")
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount} from Account {self.account_number}. New balance: {self.balance}")
        else:
            print(f"Insufficient balance in Account {self.account_number}. Current balance: {self.balance}")
    
    def display_balance(self):
        print(f"Account {self.account_number} balance: {self.balance}")


class SavingsAccount(Account):
    def __init__(self, account_number, balance=0, interest_rate=0.0):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate
    
    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        print(f"Interest earned on Account {self.account_number}: {interest}")
        return interest


class CheckingAccount(Account):
    def __init__(self, account_number, balance=0, overdraft_limit=0):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit
    
    def apply_overdraft(self, amount):
        if self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
            print(f"Overdraft applied on Account {self.account_number}. New balance: {self.balance}")
        else:
            print(f"Cannot apply overdraft on Account {self.account_number}. Exceeds overdraft limit.")


# Creating instances of SavingsAccount and CheckingAccount
johnSavings = SavingsAccount("SA001", balance=1000, interest_rate=0.05)
janeChecking = CheckingAccount("CA001", balance=500, overdraft_limit=1000)

# Depositing and withdrawing from the accounts
johnSavings.deposit(500)
janeChecking.withdraw(200)

# Calculating interest and applying overdraft
johnSavings.calculate_interest()
janeChecking.apply_overdraft(700)

# Displaying balances
johnSavings.display_balance()
janeChecking.display_balance()
