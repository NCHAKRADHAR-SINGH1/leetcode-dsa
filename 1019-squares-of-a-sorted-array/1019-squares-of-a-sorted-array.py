class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        positive=sorted(abs(x) if x <0 else x for x in nums)
        li=[]
        for i in positive:
          result=i*i
          li.append(result)
        return (li)