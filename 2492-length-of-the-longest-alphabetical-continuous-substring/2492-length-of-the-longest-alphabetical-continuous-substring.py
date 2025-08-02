class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        if len(s)==1:
            return len(s)
        count=1
        maxi=1
        for i in range(1,len(s)):
            if ord(s[i])-ord(s[i-1])==1:
                count=count+1
                maxi=max(maxi,count)
            else:
                count=1
        return maxi