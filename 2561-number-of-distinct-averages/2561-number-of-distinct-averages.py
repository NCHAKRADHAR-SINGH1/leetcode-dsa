class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        li=[]
        nums.sort()
        while len(nums) > 1:
            min_element=nums[0]
            max_element=nums[-1]
            average=(min_element+max_element)/2
            li.append(average)
            nums.pop(0)
            nums.pop(-1)
        distinct_count=len(set(li))
        return distinct_count