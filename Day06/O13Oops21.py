
from abc import ABC, abstractmethod
class Employee(ABC):

    @abstractmethod
    def PF_Account(self):
        pass

class IBMEmployee(Employee):

    def PF_Account(self):
        print("Created Accno - ######")

print("-"  * 60)

class Account(ABC):

    def __init__(self):
        print("account.....")

    @abstractmethod
    def get_balance(self):
        pass

    def deposit(self):
        pass

class SavingsAccount(Account):

    def Deposit(self):
        print("Amount credited successfully......")

    def get_balance(self):
        print("Balance in the accont is ######")

sav1 = SavingsAccount()
sav1.get_balance()