class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance


class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        print(f"Account {account.account_number} added to the bank.")

    def remove_account(self, account):
        if account in self.accounts:
            self.accounts.remove(account)
            print(f"Account {account.account_number} removed from the bank.")
        else:
            print(f"Account {account.account_number} is not found in the bank.")

    def calculate_total_balance(self):
        total_balance = sum(account.balance for account in self.accounts)
        print(f"Total balance of all accounts: {total_balance}")


# Creating instances of Account
account1 = Account("A001", 5000)
account2 = Account("A002", 10000)
account3 = Account("A003", 15000)

# Creating an instance of Bank
myBank = Bank()

# Adding accounts to the bank
myBank.add_account(account1)
myBank.add_account(account2)
myBank.add_account(account3)

# Removing an account from the bank
myBank.remove_account(account2)

# Calculating the total balance of all accounts in the bank
myBank.calculate_total_balance()
