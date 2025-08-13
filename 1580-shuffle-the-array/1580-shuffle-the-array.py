class Solution(object):
    def shuffle(self, nums, n):
         li=[]
         i=0
         j=n
         while i<=n and j < len(nums):
           li.append(nums[i])
           li.append(nums[j])
           i+=1
           j+=1
         return li
        
        