###########################################################################################################################################
# PYTHON KWARGS
###########################################################################################################################################

# Python Kwargs
# Keyword arguments -> **kwargs

def sum(**kwargs):
    sum = 0
    for key, item in kwargs.items():
        sum += item

    return round(sum, 2)


print(sum(coffee=2.99, sandwich=4.55, cake=2.99))