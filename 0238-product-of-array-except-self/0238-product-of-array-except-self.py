class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix=[1]*n
        suffix=[1]*n
        pre_result=1
        for i in range(n):
            prefix[i]=pre_result
            pre_result=pre_result*nums[i]
        suf_result=1
        for i in range(n-1,-1,-1):
            suffix[i]=suf_result
            suf_result=suf_result*nums[i]
        li=[ suffix[i]*prefix[i]    for i in range(len(suffix))]
        return li

     