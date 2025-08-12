class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        li=[]
        count=0 
        for i in range(len(s)-2):
            li.append((s[i:i+3]))
        for j in range(len(li)):
            if len(set(li[j]))==3:
                count=count+1
        return count