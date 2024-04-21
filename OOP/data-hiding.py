#single underscore
print("\nSingle Underscore")
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def _display_info(self):
        print(f"Name: {self._name}, Age: {self._age}")

    def public_method(self):
        print("This is a public method.")
        self._display_info()

person = Person("John", 30)
person.public_method()
print(person._name) 
person._display_info() 


#double underscore
print("\nDouble Underscore")
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def __update_balance(self, amount):
        self.__balance += amount

    def deposit(self, amount):
        if amount > 0:
            self.__update_balance(amount)
            print(f"Deposited: ${amount}")
        else:
            print("Invalid amount.")

    def get_balance(self):
        return f"Current balance: ${self.__balance}"

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())