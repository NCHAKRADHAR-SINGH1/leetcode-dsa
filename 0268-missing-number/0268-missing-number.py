class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i=0
        while i<len(nums):
            val=nums[i]
            if val<len(nums) and nums[val]!=nums[i]:
                nums[i],nums[val]=nums[val],nums[i]
            else:
                i=i+1
        for i,val in enumerate(nums):
            if val!=i:
                return (i)
        else:
            return len(nums)