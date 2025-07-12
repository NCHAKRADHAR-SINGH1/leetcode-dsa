class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
       string=set(allowed)
       count=0
       for word in words:
            if all(ch in string for ch in word):
                 count=count+1
       return (count)