"""
Author: Walfred Cutaran

Problem: Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
Print the decimal value of each fraction on a new line with 6 places after the decimal.

Print
Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with  digits after the decimal. The function should not return a value.

Input Format

The first line contains an integer, , the size of the array.
The second line contains (n) space-separated integers that describe arr(n)

"""

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positive_cnt = 0.0
    negative_cnt = 0.0
    zero_cnt = 0.0

    for i in range(len(arr)):
        if arr[i] > 0:
            positive_cnt += 1
        elif arr[i] < 0:
            negative_cnt += 1
        else:
            zero_cnt += 1

    print("%.6f" % float(positive_cnt / len(arr)))
    print("%.6f" % float(negative_cnt / len(arr)))
    print("%.6f" % float(zero_cnt / len(arr)))
