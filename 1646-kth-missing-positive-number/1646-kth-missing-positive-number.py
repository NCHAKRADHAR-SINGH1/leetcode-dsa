class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        li=[]
        temp=k
        for i in range(1,50000):
            if i not in arr:
                li.append(i)
                k-=1
                if k==0:
                    break
        return li[k-1]