class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = ""
        self.__balance = 0.0
        self.set_account_number(account_number)
        self.set_balance(balance)

    def set_account_number(self, account_number):
        self.__account_number = str(account_number)

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Warning: Balance cannot be negative. Balance was not changed.")

    @property
    def account_number(self):
        return self.__account_number

    @property
    def balance(self):
        return self.__balance


account = BankAccount("1234", 1500.50)

print("Account Number:", account.account_number)
print("Balance: ₱", account.balance)

# Try an invalid balance
account.set_balance(-500)

print("Balance after attempted update: ₱", account.balance)

# Try a valid balance update
account.set_balance(2750.75)
print("Updated balance: ₱", account.balance)
