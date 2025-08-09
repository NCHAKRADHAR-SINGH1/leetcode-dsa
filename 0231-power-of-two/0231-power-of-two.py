class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
      for x in range(31):
         if n==2**x:
          return True
      return False
    