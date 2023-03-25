"""
Author: Walfred Cutaran

Problem: Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.

Lily decides to share a contiguous segment of the bar selected such that:

The length of the segment matches Ron's birth month, and,
The sum of the integers on the squares is equal to his birth day.

"""

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m): # sum d conseq m
    cnt = 0
    st = m
    for i in range(len(s)):
        if sum(s[i:st]) == d:
            cnt += 1
        st += 1
            
    return cnt
