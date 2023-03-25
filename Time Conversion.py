"""
Author: Walfred Cutaran

Problem: Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

"""

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    ans = ""
    s_end = s[8:] # am or pm
    s = s[:8]
    s = s.split(':')

    if s_end == "AM":
        if s[0] == "12":
            ans += "00:"
        else:
            ans += s[0] + ':'
        
        ans += s[1] + ':'
        ans += s[2]
        return ans

    # if end == pm

    if s[0] == "12":
        ans += s[0] + ':'
        ans += s[1] + ':'
        ans += s[2]
        return ans
        
    else:
        ans += str(int(s[0]) + 12) + ':'
        ans += s[1] + ':'
        ans += s[2]
        return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
