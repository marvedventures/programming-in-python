###########################################################################################################################################
# RELOAD() FUNCTION
###########################################################################################################################################

# reload()
# -> reloads an imported module in Python, in importlib module
# -> make dynamic changes within code with import statement

###########################################################################################################################################

# NOTE: SAMPLE MODULE IS A SINGLE LINE FILE CONTAINING : print('Hello World')

import sample
import sample
import sample

'''
Code above only reload once even though it was imported three times
"Hello World"
'''

###########################################################################################################################################

import importlib

importlib.reload(sample)
importlib.reload(sample)
importlib.reload(sample)

'''
Code above runs three times.
"Hello World"
"Hello World"
"Hello World"
'''

###########################################################################################################################################
