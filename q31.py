from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, acc_no, name, balance):
        self.__acc_no = acc_no
        self.__name = name
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance")

    @abstractmethod
    def calculate_interest(self):
        pass


class SavingsAccount(Account):
    def calculate_interest(self):
        return self.get_balance() * 0.04   # 4% interest


class CurrentAccount(Account):
    def calculate_interest(self):
        return self.get_balance() * 0.02   # 2% interest


# Runtime Polymorphism
acc1 = SavingsAccount(101, "Ritom", 10000)
acc2 = CurrentAccount(102, "Rahul", 10000)

for acc in [acc1, acc2]:
    print("Interest:", acc.calculate_interest())