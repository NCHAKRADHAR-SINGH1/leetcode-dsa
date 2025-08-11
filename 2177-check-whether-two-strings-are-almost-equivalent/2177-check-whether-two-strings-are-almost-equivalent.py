class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        dici1=Counter(word1)
        dici2=Counter(word2)
        total=dici1+dici2
        for ch in total:
            diff=abs(dici1.get(ch,0)-dici2.get(ch,0))
            if diff > 3:
                return False
                break
        return True