class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        total=Counter(basket1)+Counter(basket2)
        for key,value in total.items():
            if value % 2 !=0:
                return -1
        dici1=Counter(basket1)
        dici2=Counter(basket2)
        extra1=[]
        extra2=[]
        for key in total:
            diff=dici1.get(key,0)-dici2.get(key,0)
            if diff > 0:
                extra1.extend([key]*(diff//2))
            elif diff < 0:
                extra2.extend([key]*(-diff//2))
        min_value=min(total.keys())
        cost=0
        extra1.sort()
        extra2.sort(reverse=True)
        for a,b in zip(extra1,extra2):
            cost=cost+min(a,b,2*min_value)
        return cost