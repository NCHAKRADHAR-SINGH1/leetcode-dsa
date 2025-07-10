class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
      dici1=Counter(s)
      dici2=Counter(t)
      for char in dici2:
        if dici2[char] !=dici1.get(char,0):
            return (char)  