class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dici={}
        count=0
        for i in arr:
            if i not in dici:
                dici[i]=1
            else:
                dici[i]+=1
        for i in dici:
            if dici[i]==1:
                count=count+1
                if count==k:
                    return i
        return ""
        
