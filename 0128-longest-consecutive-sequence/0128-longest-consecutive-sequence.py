class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxi=1
        seen=set()
        for i in nums:
            seen.add(i)
        for num in seen:
            if num-1 not  in seen:
                count=0
                while num in seen:
                    num+=1
                    count+=1
                    maxi=max(maxi,count)
        return maxi