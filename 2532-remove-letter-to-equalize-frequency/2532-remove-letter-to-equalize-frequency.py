from collections import Counter
class Solution:
    def equalFrequency(self, word: str) -> bool:
        dici=Counter(word)
        for ch in dici:
            dici[ch]-=1
            freq=[ ch for ch in dici.values() if ch >0 ]
               
            if len(set(freq))==1:
                return True
            else:
                dici[ch]+=1
    
        else:
            return False