class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        dici1={}  
        dici2={}
        count=0
        for i in range(len(words1)):
           dici1[words1[i]]=1+dici1.get(words1[i],0)
        for i in range(len(words2)):
            dici2[words2[i]]=1+dici2.get(words2[i],0)
        for word in dici1:
            if dici1[word]==1 and dici2.get(word,0)==1:
                count=count+1
        return count
        

