class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
     l=r=0
     while r<len(nums):
        if nums[r]!=0 and nums[l]==0:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
        if nums[l]!=0:
            l+=1
        r+=1

        