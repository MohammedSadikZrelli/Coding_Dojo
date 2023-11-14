class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_info(self):
        print(f"User: {self.name}, Email: {self.email}")
        self.account.display_account_info()
        return self

    def example_method(self):
        self.account.deposit(100)
        print(self.account.balance)
        return self
