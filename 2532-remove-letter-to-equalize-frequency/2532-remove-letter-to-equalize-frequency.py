from collections import Counter
class Solution:
    def equalFrequency(self, word: str) -> bool:
        dici=Counter(word)
        for ch in dici:
            temp=dici.copy()
            temp[ch]-=1
            if temp[ch]==0:
                del temp[ch]
            if len(set(temp.values()))==1:
                return True
    
        else:
            return False