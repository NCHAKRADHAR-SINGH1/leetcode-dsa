class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        count=1
        maxi=1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                count+=1
                maxi=max(maxi,count)
            else:
                count=1

        return maxi