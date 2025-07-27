class Solution(object):
    def stringMatching(self, words):
        result=[]
        for i in range(len(words)):
           for j in range(len(words)):
              if i==j:
                continue
              elif words[j] in words[i] and words[j] not in result:
                result.append(words[j])
        return result
        