class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        li=[]
        if s1==s2:
             return (True)
        elif len(s1)==len(s2):
            for i in range(len(s1)):
                if s1[i]!=s2[i]:
                     li.append(i)
        if len(li) > 2:
             return (False)
        elif len(li)==1:
            return False
        elif len(li)==2:
            i,j=li
            if s1[i]==s2[j] and s1[j]==s2[i]:
               return (True)
            else:
                return False
