# ALGORITHMS
###########################################################################################################################################

# Algorithms
# - series of steps to complete a given task/ solve a problem

# Parts of an algorithm
# input
# instructions
# output

###########################################################################################################################################

# Palindrome Algorithm

def isPalindrome(str):

    if str == str[::-1]:
        return True
    else:
        return False


print(isPalindrome('racecar'))

###########################################################################################################################################

# Exercise: Make a cup of coffee

# Introduction
# In this exercise, you will practice the use of an algorithm to make a cup of instant coffee. The purpose is to lay out the steps required in order to get the final product.

# Instructions
# Step 1: Start with the inputs - what is needed to make a cup of instant coffee?
# Step 2: Think about all the steps required in the physical aspect of making a cup of instant coffee.
# Step 3: Consider the edge cases of optional things like milk or sugar, some people may want it.
# Step 4: The algorithm when complete should have as its final result a cup of coffee.
# Tips: Planning is key with any algorithm. Make sure you have all the steps neatly laid out.


# Solution algorithm

# INPUT
# Ingredients required:
# 1. Cup
# 2. Hot water
# 3. Coffee granules
# Optional:
# 1. Milk
# 2. Cream
# 3. Sugar

# OUTPUT
# A cup of coffee.

# STEPS
# 1. Add drinking water to an electric kettle.
# 2. Put the kettle on to boil water.
# 3. While waiting, prepare coffee.
# 4. Add coffee granules to the cup.
# 5. If water is boiled, pour water into a cup, else continue to wait.
# 6. If milk or cream is required, add and stir.
# 7. If sugar is required, add and stir.
# 8. Return coffee.

###########################################################################################################################################

# TYPES OF ALGORITHMS

# Recursion
# - a method or a function that will call itself.
# - used to resolve problems by breaking the problem down into sub-problems.

# Divide and conquer
# - consists of two parts.
# - first is breaking the problem down into smaller sub-problems and the second is solving the final solution.

# Dynamic programming
# -  mainly used for optimization problems.
# -  similar to the divide and conquer algorithm in that it splits the problems into sub-problems.

# Greedy algorithm
# - finds the best solution in each and every step instead of approaching optimization in a global way.


###########################################################################################################################################

# FASTEST TO SLOWEST BIG-O

#  The below table showcases the fastest to slowest of these different categories:

# Constant - O(c)
# Logarithmic - O(log(n))
# Linear - O(n)
# Quadratic - O(n^2)
# Cubic - O(n^3)
# Exponential - O(2^n)
# Factorial - O(n!)

###########################################################################################################################################
