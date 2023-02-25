###########################################################################################################################################
# RECURSION
###########################################################################################################################################

# Syntax
def recursion(obj):
    # some logic
    return recursion(obj)

# Recursion - call itself multiple times, must have base condition
# For Loop - iterate

###########################################################################################################################################


# For Loop
def find_factorial_by_looping(n):
    if n < 0:
        return 0
    else:
        factorial = 1
        for item in range(1, n+1):
            factorial = factorial*item
        return factorial


print(find_factorial_by_looping(5))  # 120

###########################################################################################################################################


# Recursion
def find_factorial_by_recursive(n):
    if n == 1:
        return 1
    else:
        return n * find_factorial_by_recursive(n - 1)


print(find_factorial_by_recursive(5))  # 120

# Explanation:
# 5 * factorial(4)
# 5 * (4 * factorial(3))
# 5 * (4 * (3 * factorial(2)))
# 5 * (4 * (3 * (2 * factorial(1))))
# 5 * (4 * (3 * (2 * (1 * factorial(0)))))
# 5 * (4 * (3 * (2 * (1 * 1))))
# 5 * (4 * (3 * (2 * 1)))
# 5 * (4 * (3 * 2))
# 5 * (4 * (6))
# 5 * (24)
# 120

###########################################################################################################################################

# Recursion example: Tower of Hanoi

# Objective and rules of the puzzle
# The objective is to move n number of disks from one tower to another following a set of rules.

# These rules are as follows:
# Only one disk can be moved at a time
# Only the upper disk of any of the towers can be moved
# Larger disks cannot be placed over smaller disks


def hanoi(disks, source, helper, destination):
    # Base Condition
    if (disks == 1):
        print(f'Disk {disks} moves from tower {source} to tower {destination}.')
        return

    # Recursive calls in which function calls itself
    hanoi(disks - 1, source, destination, helper)
    print(f'Disk {disks} moves from tower {source} to tower {destination}.')
    hanoi(disks - 1, helper, source, destination)


# Driver code
disks = int(input('Number of disks to be displaced: '))
'''
Tower names passed as arguments:
Source: A
Helper: B
Destination: C
'''
# Actual function call
hanoi(disks, 'A', 'B', 'C')

# OUTPUT FOR 3 DISKS:
# Number of disks to be displaced: 3
# Disk 1 moves from tower A to tower C.
# Disk 2 moves from tower A to tower B.
# Disk 1 moves from tower C to tower B.
# Disk 3 moves from tower A to tower C.
# Disk 1 moves from tower B to tower A.
# Disk 2 moves from tower B to tower C.
# Disk 1 moves from tower A to tower C.

###########################################################################################################################################
