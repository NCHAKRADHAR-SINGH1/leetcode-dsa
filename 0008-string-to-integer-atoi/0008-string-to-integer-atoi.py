class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        if len(s)==0:
            return 0
        sign=1
        res=0
        if s[0]=='+' or s[0]=='-':
            if s[0]=='-':
                sign=-1
            s=s[1:]
        for char in s:
            if char.isdigit():
                res=res*10+int(char)
            else:
                 break
        res=res*sign
        if res < -2**31:               
            return (-2**31)
        elif res > 2**31 - 1:
             return (2**31 - 1)
        return (res)         
    