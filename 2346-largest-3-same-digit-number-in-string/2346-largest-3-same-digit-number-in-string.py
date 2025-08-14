class Solution:
    def largestGoodInteger(self, num: str) -> str:
        stack=[]
        largest=""
        for i in num:
          if len(stack) >=2 and stack[-2]==stack[-1]==i:
            result=i*3
            if result > largest:
                largest=result
            stack.clear() 
          else:
            stack.append(i)
        return largest
       
      