class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        dici=Counter({ch:float("inf") for ch in allowed})
        count=0      
        for i in range(len(words)):
            word=words[i]
            dici2=Counter(word)
            if dici>= dici2:
                count=count+1
        return (count)