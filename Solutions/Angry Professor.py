"""
Author: Walfred Cutaran

Problem: A Discrete Mathematics professor has a class of students. Frustrated with their lack of discipline, 
the professor decides to cancel class if fewer than some number of students are present when class starts. Arrival times go from on time (arrival_time <= 0) 
to arrived late (arrival_time > 0).

Given the arrival time of each student and a threshhold number of attendees, determine if the class is cancelled.
"""

#
# Complete the 'angryProfessor' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY a
#

def angryProfessor(k, a):
    # type(k): int type(a): intlist
    for value in a:
        if value <= 0:
            k -= 1
    
    if k <= 0:
        return "NO"
    return "YES"
