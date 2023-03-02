###########################################################################################################################################
# PYTHON INSTANCE METHODS
###########################################################################################################################################

# -> changes made in an instance object affect only that instance.; polymorphism(can have many forms)

###########################################################################################################################################

# PAYMENT SYSTEM

class Payslip:
    def __init__(self, name, payment, amount) -> None:
        self.name = name
        self.payment = payment
        self.amount = amount

    def pay(self):
        self.payment = 'yes'

    def status(self):
        if self.payment == 'yes':
            print(f'{self.name} has paid {self.amount}.')
        else:
            print(f'{self.name} is not paid yet.')


roger = Payslip('Roger', 'no', 1000)
nathan = Payslip('Nathan', 'no', 2000)

roger.status()  # Roger is not paid yet.
nathan.status()  # Nathan is not paid yet.


# Roger makes payment (only roger object/instance will change)
roger.pay()
roger.status()  # Roger has paid 1000.
nathan.status()  # Nathan is not paid yet.

###########################################################################################################################################
