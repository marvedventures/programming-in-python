###########################################################################################################################################
# Pandas
###########################################################################################################################################
import pandas as pd

a = pd.DataFrame({'Animals': ['Dog', 'Cat', 'Lion', 'Cow', 'Elephant'],
                  'Sounds': ['Barks', 'Meow', 'Roars', 'Moo', 'Trumpet']})

print(a)
# OUTPUT:
'''    
    Animals   Sounds
0       Dog    Barks
1       Cat     Meow
2      Lion    Roars
3       Cow      Moo
4  Elephant  Trumpet
'''


print(a.describe())
# OUTPUT:
'''
       Animals Sounds
count        5      5
unique       5      5
top        Dog  Barks
freq         1      1
'''

###########################################################################################################################################

b = pd.DataFrame({
    'Letters': ['a', 'b', 'c', 'd', 'e', 'f'],
    'Numbers': [12, 7, 9, 3, 5, 1]})

print(b.sort_values(by='Numbers'))
# OUTPUT:
'''
  Letters  Numbers
5       f        1
3       d        3
4       e        5
1       b        7
2       c        9
0       a       12
'''

b = b.assign(new_values=b['Numbers']*3)
print(b)
# OUTPUT:
'''
  Letters  Numbers  new_values
0       a       12          36
1       b        7          21
2       c        9          27
3       d        3           9
4       e        5          15
5       f        1           3
'''

###########################################################################################################################################

# CODE EXPLANATION:
'''
In the four outputs in this code, I created a pandas DataFrame in the code above called a.

    - The first output is for the DataFrame called a that displays the output in a very systematic format.
    - The second output uses the describe() function in pandas that will give the count, frequency, top values and frequency among other values.
    - In the second DataFrame, b consists of letters and numbers in random order.
    - The third output is a sorting function that will provide a sorted table leading to shuffling of the data entries in the table.
    - Lastly, the assign() function takes the values present inside the table, performs an operation over them and creates a new variable called new_values that is then added to the table.

Pandas, just like Numpy is very widely used and has a vast variety of functionalities present in addition to the ones mentioned.
'''

###########################################################################################################################################
