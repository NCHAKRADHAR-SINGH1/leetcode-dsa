class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
     
        li=s.split()
        if len(li) >= k:
          pop=li[:k]
          return (" ".join(pop))
        else:
            return s
        
        
        