class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=[]
        for ch in s:
            if len(stack)>0 and stack[-1][0]==ch:
                stack[-1][1]+=1
                if stack[-1][1]==k:
                    stack.pop()
            else:
                stack.append([ch,1])
        return "".join([ key*value for key,value in stack])