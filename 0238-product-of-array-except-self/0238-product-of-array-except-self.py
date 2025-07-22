class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix=[1]*len(nums)
        postfix=[1]*len(nums)
        pre_result=1
        for i in range(n):
          prefix[i]=pre_result
          pre_result*=nums[i]
        post_result=1
        for i in range(n-1,-1,-1):
            postfix[i]=post_result
            post_result*=nums[i]
        result=[prefix[i]*postfix[i] for i in range(n)]
        return result

     