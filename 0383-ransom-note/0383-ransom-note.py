class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dici1=Counter(ransomNote)
        dici2=Counter(magazine)
        return all(dici1[ch] <= dici2.get(ch,0) for ch in dici1)
            
