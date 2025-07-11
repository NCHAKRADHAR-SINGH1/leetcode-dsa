class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        x=list(zip(heights,names))
        x.sort(reverse=True)
        return [names for heights,names in x]