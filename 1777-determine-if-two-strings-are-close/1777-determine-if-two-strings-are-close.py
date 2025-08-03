class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
         if len(word1)!=len(word2):  return False
         set1=set(word1)
         set2=set(word2)
         if set1!=set2:   return False
         dici1=Counter(word1)
         dici2=Counter(word2)
         count1=sorted(word1.count(ch) for ch in set1)
         count2=sorted(word2.count(ch) for ch in set2)
         return count1==count2