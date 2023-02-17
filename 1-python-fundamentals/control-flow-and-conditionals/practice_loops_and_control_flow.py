###########################################################################################################################################
# PRACTICING CONTROL FLOW AND LOOPS
###########################################################################################################################################

favorites = ['Creme Brulee', 'Apple Pie',
             'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Churros':
        print('Yes! One of my favorite desserts is', dessert)
# Yes! One of my favorite desserts is Churros

###########################################################################################################################################

for dessert in favorites:
    if dessert == 'Pudding':
        print('Yes one of my favorite desserts is', dessert)
else:
    print('No sorry, that dessert is not on my list')
# No sorry, that dessert is not on my list

# The code works as intended but you may notice one flaw.
# If you change the search term to something that is on the list like "Churros"
# and run it again you will get the following output:
# Yes one of my favorite desserts is Churros
# No sorry, not a dessert on my list

for dessert in favorites:
    if dessert == 'Churros':
        print('Yes one of my favorite desserts is', dessert)
else:
    print('No sorry, that dessert is not on my list')
# Yes one of my favorite desserts is Churros
# No sorry, not a dessert on my list
# NOTE: NEED BREAK STATEMENT TO FIX

###########################################################################################################################################

# LOOP CONTROL STATEMENTS

# 1. BREAK
# - used to stop the loop, which in turn also stops the else condition

for dessert in favorites:
    if dessert == 'Churros':
        print('Yes one of my favorite desserts is', dessert)
        break
else:
    print('No sorry, not a dessert on my list')
# Yes one of my favorite desserts is Churros

###########################################################################################################################################

# 2. CONTINUE
# - similar to break, continue can be used to control the iteration of the loop.
# - the key difference is that it can allow you to skip over a section of the loop but then continue on with the rest.

for dessert in favorites:
    if dessert == 'Churros':
        continue
    print('Other desserts I like are', dessert)
# Other desserts I like are Creme Brulee
# Other desserts I like are Apple Pie
# Other desserts I like are Tiramisú
# Other desserts I like are Chocolate Cake

###########################################################################################################################################

# 3. PASS
# - allows you to run through the loop in its entirety and effectively ignore that the if condition has been satisfied.

for dessert in favorites:
    if dessert == 'Churros':
        pass
    print('Other desserts I like are', dessert)
# Other desserts I like are Creme Brulee
# Other desserts I like are Apple Pie
# Other desserts I like are Churros
# Other desserts I like are Tiramisú
# Other desserts I like are Chocolate Cake

# - it is also used to create a placeholder for future code:
# when the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.
# empty code is not allowed in loops, function definitions, class definitions, or in if statements.


def myfunction():
    pass


class Person:
    pass


a = 33
b = 200

if b > a:
    pass
