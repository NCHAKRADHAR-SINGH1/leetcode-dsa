class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        groups=[]
        for i in range(0,len(s),k):
            group=s[i:i+k]
            groups.append(group)
        remain_group=groups[-1]
        for i in range(k):
            if len(remain_group)!=k:
                remain_group+=fill
        groups[-1]=remain_group
        return groups