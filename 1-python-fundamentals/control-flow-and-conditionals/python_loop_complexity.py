###########################################################################################################################################
# NESTED LOOPS AND THE EFFECT ON TIME COMPLEXITY
###########################################################################################################################################
import time

start_time = time.time()

# outer loop
for x in range(100):
    # inner loop
    for y in range(1000):
        print(0, end=' ')
    print()

print(round((time.time() - start_time), 0), 'seconds')

# in each iteration of outer loop,
# it will print 0 (1000 times) in the inner loop
# before proceeding with the next iteration in the outer loop until 100

###########################################################################################################################################
