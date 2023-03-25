"""
Author: Walfred Cutaran

Problem: Given an array of bird sightings where every element represents a bird type id, determine the id of the most frequently sighted type. 
If more than 1 type has been spotted that maximum amount, return the smallest of their ids.

Example:
arr = [1, 1, 2, 2, 3]
There are two each of types 1 and 2, and one sighting of type 3. Pick the lower of the two types seen twice: type 1.

"""

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    dic = {}
    for value in arr:
        if value in dic:
            dic[value] += 1
        else:
            dic[value] = 1
    
    ans = [key for key, val in dic.items() if val == max(dic.values())]
    return min(ans)
