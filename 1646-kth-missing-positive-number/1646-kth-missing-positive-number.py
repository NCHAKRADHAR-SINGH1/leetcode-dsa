class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arr_set = set(arr)
        temp=k
        li = []
        for i in range(1, 50000):  # just needs to be high enough
            if i not in arr_set:
                li.append(i)
                k-=1
                if k==0:
                    break
        return li[temp-1]
        
