class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res=[]
        dici1=Counter(words[0])
        for i in range(1,len(words)):
            dici2=Counter(words[i])
            for ch in dici1:
                dici1[ch]=min(dici1[ch],dici2[ch])
        for key,value in dici1.items():
            res.extend([key]*value)
        return res

        
        r