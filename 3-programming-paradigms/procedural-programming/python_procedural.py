###########################################################################################################################################
# WHAT IS PROCEDURAL PROGRAMMING
###########################################################################################################################################

# Procedural Programming
# - writing step by step instructions
# - structures code into procedures (sub-routine)
# - logical steps

# Pros
# easy to learn
# reusable
# easy to understand

# Cons
# hard to maintain
# doesn't relate well
# exposed data

###########################################################################################################################################

# PROCEDURAL PROGRAMMING EXAMPLE

# procedures(sub-routine)
def bill_total(bill):
    total = 0.00
    for k, v in bill.items():
        total += v
    return total


# procedures(sub-routine)
def calculate_tax(percent, bill_total):
    return round((percent*bill_total)/100.0, 2)


# procedures(sub-routine)
food_bill = {
    1: 3.99,
    2: 4.55,
    3: 11.99,
    4: 22.00,
    5: 2.00
}

# procedures(sub-routine)
food_total = bill_total(food_bill)

# procedures(sub-routine)
tax_total = calculate_tax(15, food_total)

# procedures(sub-routine)
print('Overall:', food_total + tax_total)

###########################################################################################################################################
