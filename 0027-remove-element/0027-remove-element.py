class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
      start=0
      end=len(nums)-1
      while start <=end:
         if nums[start]==val:
             nums[start],nums[end]=nums[end],nums[start]
             end=end-1
         else:
            start=start+1
      return (start)
    