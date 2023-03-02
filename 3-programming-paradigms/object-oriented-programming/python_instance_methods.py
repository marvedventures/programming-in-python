###########################################################################################################################################
# PYTHON INSTANCE METHODS
###########################################################################################################################################

# -> changes made in an instance object affect only that instance.

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
            return f'{self.name} has paid {self.amount}.'
        else:
            return f'{self.name} is not paid yet.'


roger = Payslip('Roger', 'no', 1000)
nathan = Payslip('Nathan', 'no', 2000)

print(roger.status())  # Roger is not paid yet.
print(nathan.status())  # Nathan is not paid yet.


# Roger makes payment (only roger object/instance will change)
roger.pay()
print(roger.status())  # Roger has paid 1000.
print(nathan.status())  # Nathan is not paid yet.

###########################################################################################################################################
