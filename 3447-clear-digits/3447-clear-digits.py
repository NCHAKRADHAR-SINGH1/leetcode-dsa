class Solution(object):
    def clearDigits(self, s):
        if all(ch.isalpha() for ch in s):
            return s
        stack=[]
        for i in s:
            if stack and i.isdigit() and stack[-1].isalpha():
                stack.pop(-1)
            else:
                stack.append(i)
        return  "".join( ch for ch in stack)