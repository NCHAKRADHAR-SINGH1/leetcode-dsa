class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dici=Counter(nums)
        li=[]
        for ch in dici:
            if dici[ch]==1:
                li.append(ch)
        return sum(li)

        
