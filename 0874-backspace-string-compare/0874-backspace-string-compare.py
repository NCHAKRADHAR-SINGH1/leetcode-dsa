class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def string(s):
            stack=[]
            for ch in s:
                if stack and ch=='#':
                      stack.pop()
                elif len(stack)==0 and ch=='#':
                    continue
                else:
                    stack.append(ch)
            return ''.join(stack)
        return string(s)==string(t)
            