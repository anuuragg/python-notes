class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.__account_number = account_number
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}. Current balance: ${self.__balance}")
        else:
            print("Invalid amount. Cannot deposit.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: ${amount}. Current balance: ${self.__balance}")
        else:
            print("Invalid amount. Cannot withdraw.")

    def get_balance(self):
        return f"Current balance: ${self.__balance}"

account = BankAccount("12345678", 500)

account.deposit(200)
account.withdraw(100)
print(account.get_balance())

