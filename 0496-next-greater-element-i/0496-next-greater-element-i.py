class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
       stack=[]
       res=[-1]*len(nums2)
       for idx,val in enumerate(nums2):
            while stack and stack[-1][0]<val:
                value,index=stack.pop()
                res[index]=val
            stack.append([val,idx])
       dici=dict(zip(nums2,res)) 
       final_result=[]
       for i in nums1:
            if i in dici:
                final_result.append(dici[i]) 
       return final_result