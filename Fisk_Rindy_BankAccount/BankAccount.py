class BankAccount:
    account_list = []

    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.account_list.append(self)
        
    def deposit(self, amount):
        self.balance += amount
        return self
        
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
        
    def display_account_info(self):
        print(f"Your current balance is {self.balance}")
        # print(f"Balance: $100")
        return self
        
    def yield_interest(self):
        if self.balance >= 0:
            print(f"Your current interest rate is {self.int_rate}")
        return self

    @classmethod
    def all_accounts(cls):
        for account in cls.account_list:
            account.display_account_info()


account1=BankAccount(0.01,250)
account1.yield_interest().deposit(300).deposit(20).display_account_info().deposit(55).withdraw(275)
account2=BankAccount(0.0098,465)
account2.deposit(400).deposit(942).withdraw(57).withdraw(520).withdraw(600).yield_interest().display_account_info()
