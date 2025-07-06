class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n=len(s)
        t=['']*n
        for i in range(0,n):
             t[indices[i]]=s[i]
        output=''.join(t)
        return output