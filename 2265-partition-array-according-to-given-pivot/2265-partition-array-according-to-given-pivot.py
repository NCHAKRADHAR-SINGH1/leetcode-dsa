class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        list1=[]
        list2=[]
        list3=[]
        for i in nums:
            if i < pivot:
                list1.append(i)
            elif i==pivot:
                list2.append(i)
            else:
                list3.append(i)  
        return list1+list2+list3