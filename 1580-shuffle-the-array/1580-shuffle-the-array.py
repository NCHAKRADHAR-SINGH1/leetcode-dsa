class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        list1=nums[:n]
        list2=nums[n:]
        li=[]
        for i in range(len(list1)):
           li.append(list1[i])
           li.append(list2[i])
        return (li)