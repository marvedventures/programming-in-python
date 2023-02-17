###########################################################################################################################################
# PYTHON LOOPS
###########################################################################################################################################

# FOR LOOP
# -  used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string)
# -  number of iterations already known.
for item in range(10):
    print(item)

favorites = ['Creme Brulee', 'Apple Pie',
             'Churros', 'Tiramisú', 'Chocolate Cake']

for item in favorites:
    print(item)

# can access index using enumerate()
for idx, item in enumerate(favorites):
    print(idx, item)

###########################################################################################################################################


# WHILE LOOP
# - can execute a set of statements as long as a condition is true
# - no prior information on the number of iterations.

count = 5

while count < len(favorites):
    print('I like ...', favorites[count])
    count += 1
