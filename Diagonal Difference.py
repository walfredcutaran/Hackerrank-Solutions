"""
Author: Walred Cutaran

Problem: Given a square matrix, calculate the absolute difference between the sums of its diagonals.

1 2 3
4 5 6
9 8 9

The left-to-right diagonal = 1 + 5 + 9 = 15. The right to left diagonal = 3 + 5 + 9 = 17. Their absolute difference is 2.

"""

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    ans = 0
    for i in range(len(arr)):
        ans += arr[i][i]
    for i in range(len(arr)):
        ans -= arr[i][(len(arr)-1)-i]
    
    return abs(ans)
