class Solution:
    def largestGoodInteger(self, num: str) -> str:
        stack=[]
        largest=[]
        for i in num:
          if len(stack) >=2 and stack[-2]==stack[-1]==i:
             largest.append(i*3)
             stack.clear()
          else:
            stack.append(i)
        if not largest:
            return ""
        return max(largest)
      