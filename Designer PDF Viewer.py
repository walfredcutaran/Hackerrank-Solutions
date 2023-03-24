"""
Author: Walfred Cutaran

Problem: When a contiguous block of text is selected in a PDF viewer, the selection is highlighted with a blue rectangle. 
In this PDF viewer, each word is highlighted independently.

There is a list of 26 character heights aligned by index to their letters. For example, 'a' is at index 0 and 'z' is at index 25. 
There will also be a string. Using the letter heights given, determine the area of the rectangle highlight in (mm)**2 assuming all letters are 1mm wide.

h = [1,3,1,3,1,4,1,3,2,5,5,5,5,1,1,5,5,1,5,2,5,5,5,5,5,5]
word = str(torn)
t = 2 o = 1 r = 1 n = 1

The tallest letter is 2 high and there are 4 letters. The hightlighted area will be  so the answer is 2 * 4 = 8.
"""

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    # type(h): list type(word): string
    letters = "abcdefghijklmnopqrstuvwxyz"
    lst = []
    ans = []
    for i in range(len(word)):
        for index, value in enumerate(letters):
            if word[i] == value:
                lst.append(index)
                break
    
    for elem in lst:
        ans.append(h[elem])
        
    return max(ans) * len(word)
