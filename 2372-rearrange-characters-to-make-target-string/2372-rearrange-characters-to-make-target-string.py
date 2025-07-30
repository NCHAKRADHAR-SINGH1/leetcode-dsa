class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        dici1=Counter(s)
        dici2=Counter(target)
        result=min(dici1[ch]//dici2[ch] for ch in dici2)
        return result

        