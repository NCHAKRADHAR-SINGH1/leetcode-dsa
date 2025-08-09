class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dici=Counter(arr1)
        li=[]
        for key in arr2:
            li.extend([key]*dici[key])
        res=[]
        for key in arr1:
            if key not in li:
                res.append(key)
        res.sort()
        return li+res
