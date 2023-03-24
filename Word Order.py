"""
Author: Walfred Cutaran

Problem: You are given  words. Some words may repeat. For each word, output its number of occurrences. 
The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

Note: Each input line ends with a "\n" character.

Input Format:
The first line contains the integer, (n)
The next  lines each contain a word.

Output Format
Output  lines.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.
"""

n = int(input())
my_dict = {}
word_list = []

for i in range(n):
    string = input()
    word_list.append(string)
    
    if string in my_dict:
        my_dict[string] += 1
    else:
        my_dict[string] = 1
        
print(len(my_dict))
print(' '.join([str(my_dict[word]) for word in my_dict]))
