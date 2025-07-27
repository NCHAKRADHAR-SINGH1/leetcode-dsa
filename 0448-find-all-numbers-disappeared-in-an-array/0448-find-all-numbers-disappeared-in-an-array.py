class Solution(object):
    def findDisappearedNumbers(self, nums):
        i=0
        while i<len(nums):
            val=nums[i]-1
            if val<len(nums) and nums[i]!=nums[val]:
              nums[i],nums[val]=nums[val],nums[i]
            else:
              i+=1
        res=[]
        for i,val in enumerate(nums):
            if i+1!=val:
                res.append(i+1)
        return res

        