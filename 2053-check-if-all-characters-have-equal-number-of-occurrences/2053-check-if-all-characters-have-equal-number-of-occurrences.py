class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dici={}
        for r in range(len(s)):
            dici[s[r]]=1+dici.get(s[r],0)
        if len(set(dici.values()))==1:
            return True
        else:
            return False