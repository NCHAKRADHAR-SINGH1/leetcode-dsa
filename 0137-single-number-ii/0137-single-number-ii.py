class Solution:
    def singleNumber(self, nums: List[int]) -> int:
          dici={}
          for r in range(len(nums)):
            dici[nums[r]]=1+dici.get(nums[r],0)
          for i,val in enumerate(nums):
                if dici[val]==1:
                   return    (val)