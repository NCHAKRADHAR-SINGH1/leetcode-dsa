class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        dici1=Counter(''.join( ch.lower()  for ch in licensePlate if ch.isalpha()))
        res=[]
        for i in range(len(words)):
            dici2=Counter(words[i])
            if all(dici2[ch] >=dici1[ch]   for ch in dici1):
                res.append(words[i])
        shortest_word=min(res,key=len)
        return shortest_word