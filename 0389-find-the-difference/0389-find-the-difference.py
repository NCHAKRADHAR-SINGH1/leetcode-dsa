class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
      dici1=Counter(s)
      dici2=Counter(t)
      for ch in dici2:
        if dici2[ch] !=dici1.get(ch,0):
            return (ch)  