class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count=0
        dici={'type':0,'color':0,'name':0}
        for i in range(len(items)):
            list1=items[i]
            dici['type']=list1[0]
            dici['color']=list1[1]
            dici['name']=list1[2]
            if dici[ruleKey]==ruleValue:
                count=count+1
        return count