###########################################################################################################################################
# PYTHON CONTROL FLOW
###########################################################################################################################################

# CONDITIONAL STATEMENTS

# if
# elif (else if)
# else

bill_total = 2

discount1 = 10
discount2 = 20

if bill_total > 200:
    bill_total -= discount2
    print(
        f'Your bill is ${bill_total}. You had a discount of ${discount2}.')

elif bill_total > 100:
    bill_total -= discount1
    print(f'Your bill is ${bill_total}. You had a discount of ${discount1}.')

else:
    print(f'Your bill is ${bill_total}. You had no discount.')

###########################################################################################################################################

# LOOP STATEMENTS

# for
# while
