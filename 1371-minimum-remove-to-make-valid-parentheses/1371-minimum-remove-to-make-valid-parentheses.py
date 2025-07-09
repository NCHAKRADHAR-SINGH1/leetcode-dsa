
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
       stack=[]
       seen=list()
       for i,val in enumerate(s):
            if val=='(':
                 stack.append(i)
            elif val==')':
                if stack and s[stack[-1]]=='(':
                    stack.pop()
                else:
                    stack.append(i)
       while stack:
            a=stack.pop()
            seen.append(a)
       res=""
       for i,val in enumerate(s):
            if i not in seen:
                res=res+val
       return res


        

        