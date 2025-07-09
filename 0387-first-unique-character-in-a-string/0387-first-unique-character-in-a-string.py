class Solution:
    def firstUniqChar(self, s: str) -> int:
        dici={}
        for r in range(len(s)):
           dici[s[r]]=1+dici.get(s[r],0)
        for idx,ch in enumerate(s):
            if dici[ch]==1:
               return (idx)
               break
        else:
              return (-1)