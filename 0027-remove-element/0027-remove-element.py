class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        s=nums.copy()
        nums.clear()
        for i in s:
            if i!=val:
              nums.append(i)
        return len(nums)
    