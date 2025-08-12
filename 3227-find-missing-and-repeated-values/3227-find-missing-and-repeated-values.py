class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        m=len(grid[0])
        n=len(grid)
        nums=[]
        for i in range(m):
            for j in range(n):
                nums.append(grid[i][j])
        dici=Counter(nums)
        li=[]
        max_element=max(dici.values())
        for key,value in dici.items():
            if max_element==value:
                li.append(key)
        for i in range(1,len(nums)+1):
            if i not in nums:
                li.append(i)
        return li


