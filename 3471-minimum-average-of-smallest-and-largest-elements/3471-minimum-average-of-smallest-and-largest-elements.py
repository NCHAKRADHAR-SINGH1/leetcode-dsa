class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        li=[]
        nums.sort()
        while len(nums) > 1:
            min_element=nums[0]
            max_element=nums[-1]
            average=(max_element+min_element)/2
            li.append(average)
            nums.pop(0)
            nums.pop(-1)
        return min(li)