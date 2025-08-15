class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[1]*n
        pre_result=1
        for i in range(n):
            res[i]=pre_result
            pre_result=pre_result*nums[i]
        suf_result=1
        for i in range(n-1,-1,-1):
            res[i]*=suf_result
            suf_result=suf_result*nums[i]
        return res
       
     