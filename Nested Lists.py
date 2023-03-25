"""
Author: Walfred Cutaran

Problem: Given the names and grades for each student in a class of (n) students, 
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

"""

if __name__ == '__main__':
    score_lst = [] # contains score
    lst = []
    ans = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        score_lst.append(score)
        lst.append([name, score])
        
    remove_dupli = []
    [remove_dupli.append(value) for value in score_lst if value not in remove_dupli]
    x = sorted(remove_dupli)
    min_val = x[1]
    
    for i in range(len(lst)):
        if min_val == lst[i][1]:
            ans.append(lst[i][0])
            
    for elem in sorted(ans):
        print(elem)
    
