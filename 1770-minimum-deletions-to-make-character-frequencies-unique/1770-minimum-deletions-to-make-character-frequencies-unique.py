class Solution:
    def minDeletions(self, s: str) -> int:
        seen=set()
        deletions=0
        dici=Counter(s)
        for key,value in dici.items():
            while value  > 0  and value in seen:
                value-=1
                deletions+=1
            seen.add(value)
        return deletions
