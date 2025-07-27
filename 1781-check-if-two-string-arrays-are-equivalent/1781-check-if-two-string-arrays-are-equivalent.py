class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        x=""
        x1=""
        for i in range(len(word1)):
            s1=word1[i]
            x=x+"".join(word1[i])
        for i in range(len(word2)):
           s2=word2[i]
           x1=x1+"".join(word2[i])
        return (x==x1)