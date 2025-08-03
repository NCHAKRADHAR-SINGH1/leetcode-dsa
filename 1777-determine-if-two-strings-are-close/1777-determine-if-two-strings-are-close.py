class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
         set1=set(word1)
         set2=set(word2)
         if set1!=set2:
            return False
         dici1=Counter(word1)
         dici2=Counter(word2)
         return  (sorted(dici1.values())==sorted(dici2.values()) )