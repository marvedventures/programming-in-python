###########################################################################################################################################
# NumPy
###########################################################################################################################################

import numpy as np

a = np.zeros(10)
print(a)  # [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

b = np.full((2, 10), 0.7)
# [[0.7 0.7 0.7 0.7 0.7 0.7 0.7 0.7 0.7 0.7][0.7 0.7 0.7 0.7 0.7 0.7 0.7 0.7 0.7 0.7]]
print(b)

c = np.linspace(0, 25, 7)
# [ 0.          4.16666667  8.33333333 12.5        16.66666667 20.83333333  25.        ]
print(c)

print(type(c))  # <class 'numpy.ndarray'>

'''
Explanation: 

- The zeros() function inside numpy creates an array with n number of zeroes inside it.
- The full() function creates a two-dimensional matrix of dimensions 2 x 10 consisting only of the values 0.7.
- In the example, linspace() function divides the values between 0 and 25 in 7 equal parts. The resultant matrix is in the output.
- Finally, when you see the data type of c, it is a special data-type created and used in numpy called as ndarray. If you try the output for a and b, it will also be ndarray as numpy deals exclusively with ndarray, which is a substitute for lists and is far more efficient. 
'''

###########################################################################################################################################
