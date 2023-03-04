###########################################################################################################################################
# PYTHON BANK APP (OOP)
###########################################################################################################################################

# Import ABC and abstractmethod from the module abc (which stands for abstract base classes)
from abc import ABC, abstractmethod


# Class Bank (Abstract Bank Class)
class Bank(ABC):

    def basicinfo(self):
        print('This is a generic bank')
        return 'Generic bank: 0'

    @abstractmethod
    def withdraw(self):
        pass

    @abstractmethod
    def deposit(self):
        pass


# Class Swiss (A specific type of bank than derives from class Bank)
class Swiss(Bank):
    def __init__(self) -> None:
        super().__init__()
        self.bal = 1_000

    def basicinfo(self):
        print('This is a Swiss Bank')
        return f'Swiss Bank: {self.bal}'

    def withdraw(self, amount):
        if amount <= self.bal:
            self.bal -= amount
            print(f'Withdrawn amount: {amount}')
            print(f'New balance: {self.bal}')
        else:
            print('Insufficient funds')
        return self.bal

    def deposit(self, amount):
        self.bal += amount
        print(f'Deposited amount: {amount}')
        print(f'New Balance: {self.bal}')
        return self.bal


# Driver Code
def main():
    assert issubclass(Bank, ABC), 'Bank must derive from class ABC'
    s = Swiss()
    print(s.basicinfo())
    s.withdraw(30)
    s.withdraw(1_000)
    s.deposit(1_000)
    s.withdraw(1_500)


if __name__ == '__main__':
    main()
