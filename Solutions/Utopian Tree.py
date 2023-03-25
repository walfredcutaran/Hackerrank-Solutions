"""
Author: Walfred Cutaran

Problem: The Utopian Tree goes through 2 cycles of growth every year. Each spring, it doubles in height. Each summer, its height increases by 1 meter.

A Utopian Tree sapling with a height of 1 meter is planted at the onset of spring. How tall will the tree be after (N) growth cycles?

"""
#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def utopianTree(n):
    ans = 0
    for i in range(n+1):
        if i == 0:
            pass
        if i % 2 == 0: # even summer
            ans += 1
        if i % 2 != 0: # odd spring
            ans *= 2    
    return ans
