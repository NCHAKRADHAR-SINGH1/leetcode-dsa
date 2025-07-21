class Solution:
    def makeFancyString(self, s: str) -> str:
        res=[]
        for i in range(len(s)):
            if len(res) >= 2 and res[-1]==res[-2]==s[i]:
                continue
            else:
                res.append(s[i])
        return ''.join(res)