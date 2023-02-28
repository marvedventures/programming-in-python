###########################################################################################################################################
# MAP AND FILTER
###########################################################################################################################################

# map() -> applies to every item in iterable, return will be a map object
# filter() -> returns all elements of an iterable when function returns True, return will be a filter object

# NOTE: map and filter object can be iterated directly using for loop

coffee = ['cappucino', 'espresso', 'mocha', 'americano',
          'arabica', 'latte', 'macchiato', 'cortado']


def find_coffee(coffee):
    if coffee[0] == 'c':
        return coffee


# map()
map_coffee = map(find_coffee, coffee)
print(map_coffee)  # <map object at 0x000001F651B6BA60>

# print(list(map_coffee))
# ['cappucino', None, None, None, None, None, None, 'cortado']

for coffee in map_coffee:
    print(coffee)
    # OUTPUT:
    # cappucino
    # None
    # None
    # None
    # None
    # None
    # None
    # cortado


###########################################################################################################################################

# filter()

coffee1 = ['cappucino', 'espresso', 'mocha', 'americano',
           'arabica', 'latte', 'macchiato', 'cortado']

filter_coffee = filter(find_coffee, coffee1)
print(filter_coffee)  # <filter object at 0x000001F651B6BA00>

# print(list(filter_coffee))
# ['cappucino', 'cortado']

for coffee in filter_coffee:
    print(coffee)
    # OUTPUT:
    # cappucino
    # cortado

###########################################################################################################################################

a = [1, 2, 3]
print(list(map(str, a)))  # ['1', '2', '3']
print(''.join(list(map(str, a))))  # '123'

b = [[96], [69]]
print(list(map(str, b)))  # ['[96]', '[69]']
print(''.join(list(map(str, b))))  # '[96][69]'

###########################################################################################################################################
