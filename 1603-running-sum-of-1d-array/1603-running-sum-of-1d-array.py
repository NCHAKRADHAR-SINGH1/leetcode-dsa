class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n=len(nums)
        output=0
        li=[0]*len(nums)
        for i in range(n):
            output+=nums[i]
            li[i]=output
        return li