class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=float("-inf")
        currsum=0
        for i in range(len(nums)):
            currsum+=nums[i]
            max_sum=max(max_sum,currsum)
            if currsum<0:
               currsum=0
        return max_sum
        