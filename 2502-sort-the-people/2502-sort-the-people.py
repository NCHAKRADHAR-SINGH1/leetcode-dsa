class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        x=list(zip(names,heights))
        x.sort(key=lambda x:x[1],reverse=True)
        return [names for names,heights in x]