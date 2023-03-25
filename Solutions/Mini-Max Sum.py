"""
Author: Walfred Cutaran

Problem: Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Example
arr = [1, 3, 5, 7, 9]
The minimum sum is 1 + 3 + 5 + 7 = 16 and the maximum sum is 3 + 5 + 7 + 9 = 24. The function prints
16 24
"""

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
     arr_1 = sorted(arr)
     arr_2 = sorted(arr)
     max_val = 0
     min_val = 0
     
     arr_1.pop()
     min_val = sum(arr_1)
     
     arr_2.pop(0)
     max_val = sum(arr_2)
     
     print(min_val, max_val)

