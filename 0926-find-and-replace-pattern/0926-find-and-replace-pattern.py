class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def isomorphic(word,pattern):
            m1={}
            m2={}
            if len(word)!=len(pattern):
                return False
            for i in range(len(word)):
                a=word[i]
                b=pattern[i]
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
        res=[]
        for i in range(len(words)):
            if isomorphic(words[i],pattern):
                res.append(words[i])
        return (res)  