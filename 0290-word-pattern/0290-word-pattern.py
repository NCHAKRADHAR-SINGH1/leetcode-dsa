class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split()
        m1={}
        m2={}
        if len(s)!=len(pattern):
            return False
        for i in range(len(s)):
            a=pattern[i]
            b=s[i]
            if a in m1:
                if m1[a]!=b:
                    return False
            else:
                m1[a]=b

            if b in m2:
                if m2[b]!=a:
                    return False
            else:
                m2[b]=a
        return True
