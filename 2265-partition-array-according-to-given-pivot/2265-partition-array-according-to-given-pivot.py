class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        list1=[]
        for i in nums:
            if i < pivot:
                list1.append(i)
        for i in nums:
            if i==pivot:
                list1.append(i)
        for i in nums:
            if i > pivot:
                list1.append(i)  
        return list1