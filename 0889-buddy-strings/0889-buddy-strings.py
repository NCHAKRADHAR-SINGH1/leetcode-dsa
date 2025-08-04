from collections import Counter
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
           return False
        dici=Counter(s)
        if s==goal:
            if all(dici[ch]==1 for ch in dici):
                return False
            else:
                return True
        li=[]
        if s!=goal:
            for i in range(len(s)):
                if s[i]!=goal[i]:
                    li.append(i)
        if len(li) > 2:
            return False
        elif len(li)==1:
            return False
        elif len(li)==2:
            i,j=li
            if s[i]==goal[j] and s[j]==goal[i]:
                return True
            else:
                return False
           