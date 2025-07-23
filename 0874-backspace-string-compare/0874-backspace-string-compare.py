class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def string(s):
            stack=[]
            for ch in s:
                if ch=='#':
                    if stack:
                      stack.pop()
                else:
                    stack.append(ch)
            return ''.join(stack)
        return string(s)==string(t)
            