###########################################################################################################################################
# STORING FILE CONTENTS IN DATA STRUCTURES
###########################################################################################################################################
import random

f = open('./2-python-fundamentals/errors-exceptions-and-file-handling/petnames.txt', 'r')

f_content = f.read()
print(f_content)

f_content_list = f_content.split('\n')
print(f_content_list)
# OUTPUT:
# ['Ace', 'Atlas', 'Bailey', 'Bear', 'Blaze', 'Boomer', 'Buddy', 'Coco', 'Cooper', 'Duke', 'Dozer', 'Echo', 'Gizmo', 'Harley', 'Mac', 'Max', 'Milo', 'Oscar', 'Rex', 'Rocky', 'Rocket', 'Wolfie']

# random.choice() accepts a sequence params
print(random.choice(f_content_list))
# OUTPUT:
# random names in the list

###########################################################################################################################################

# BONUS: ASKING FOR INPUT FROM USER REGARDING WHAT FILE

# f_name = input('Type the file name: ')
# # 'r' omitted as it's the default
# f = open('./2-python-fundamentals/errors-exceptions-and-file-handling/'+f_name)
# f_content = f.read()
# f_content_list = f_content.split('\n')
# print(random.choice(f_content_list))

###########################################################################################################################################
