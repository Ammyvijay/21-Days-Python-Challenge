"""
Notes :

In n Python, attributes are variables that hold data within a class. They can be accessed using the dot notation and can be either public or private. Public attributes are accessible outside of the class, while private attributes are not.

It's important to note that Python does not enforce true private attributes, and they can still be accessed from outside the class. The single underscore prefix is simply a naming convention that signals to other programmers that the attribute or method should not be used outside the class. 

(If you're interested look up 'name mangling' in the context of a double underscore prefix)

Using attributes in Python provides a way to store, organize, and protect data within an object.

"""


class BankAccount:

    def __init__(self, name: str, accno: int, amount: int) -> None:
        self.name = name
        self.accountno = accno
        self.balance = amount
    
    def __str__(self) -> str:
        print(f"Hi {self.name}, your account is activated! your balance is {self.balance}")

    def withdraw(self,amount:int):
        if self.balance>amount:
            self.balance-=amount
            print(f"Successfully {amount} Amount is withdraw")
        else:
            print("Insufficient balance in your account")

    def deposit(self,amount:int):
        self.balance+=amount
        print(f"Successfully amount {amount} is deposited, Total balance is {self.balance}")

    def acc_balance(self):
        print(f"Current balance is {self.balance}")


bank = BankAccount("Ammy",1001,1000)
bank.acc_balance()
bank.deposit(2000)
bank.withdraw(3000)
bank.withdraw(1000)
bank.deposit(2000)
bank.acc_balance()