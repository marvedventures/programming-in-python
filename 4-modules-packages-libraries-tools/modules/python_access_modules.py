###########################################################################################################################################
# ACCESSING MODULES IN PYTHON
###########################################################################################################################################

# import user-defined modules
import python_modules

# import built-in modules
import calendar
import sys


# Location of python files
locations = sys.path

for location in locations:
    print(location)
    # C:\Users\myuser\AppData\Local\Programs\Python\Python311\python311.zip
    # C:\Users\myuser\AppData\Local\Programs\Python\Python311\Lib
    # C:\Users\myuser\AppData\Local\Programs\Python\Python311\DLLs
    # C:\Users\myuser\AppData\Local\Programs\Python\Python311
    # C:\Users\myuser\AppData\Local\Programs\Python\Python311\Lib\site-packages


# Number of leapdays between specified years
leap_days = calendar.leapdays(2000, 2015)
print(leap_days)  # 4


# Is it a Leap year?
is_leap = calendar.isleap(2000)
print(is_leap)  # True
