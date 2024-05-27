
from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def doJob(self):
        pass


class Manager(Employee):

    def doJob(self):
        print("Managers job.......")


class Testing(Employee):

    def doJob(self):
        print("Testing job.......")


def BankJob(emp):
    print("Bank Job started........")
    emp.doJob()
    print("Bank Job ended.......")
    print("-" * 60)

micheal = Manager()
tina = Testing()

BankJob(micheal)
BankJob(tina)

