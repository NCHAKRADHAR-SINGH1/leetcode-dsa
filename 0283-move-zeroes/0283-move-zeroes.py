class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
      s=nums.copy()
      nums.clear()
      for i in s:
        if i!=0:
            nums.append(i)
      a=s.count(0)
      nums.extend([0]*a)

        