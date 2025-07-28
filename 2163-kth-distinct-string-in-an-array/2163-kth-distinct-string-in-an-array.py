class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dici={}
        for i in range(len(arr)):
            dici[arr[i]]=1+dici.get(arr[i],0)
        result=[]
        for key,value in dici.items():
            if value==1:
                result.append(key)
        if len(result) >= k:
            return result[k-1]
        else:
            return ""
