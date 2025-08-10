class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dici1=Counter(nums)
        if len(set(dici1.values()))==1:
            return len(nums)
        li=[]
        most_frequent=max(dici1.values())
        for key,value in dici1.items():
            if value==most_frequent:
                li.append(value)
            
            
        return sum(li)
        
            
