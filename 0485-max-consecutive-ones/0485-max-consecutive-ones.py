class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi=0
        count=0
        for i in nums:
            if i==1:
                count=count+1
                maxi=max(maxi,count)
            else:
                count=0
        return maxi
