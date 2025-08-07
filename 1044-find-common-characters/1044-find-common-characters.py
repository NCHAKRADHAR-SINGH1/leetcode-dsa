from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        dici1=Counter(words[0])
        for i in range(1,len(words)):
            dici2=Counter(words[i])
            for ch in dici1:
                dici1[ch]=min(dici1.get(ch,0),dici2.get(ch,0))
        li=[]
        for key,value in dici1.items():
            li.extend([key]*value)
        return li

      