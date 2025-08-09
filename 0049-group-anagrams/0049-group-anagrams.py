class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram={}
        for i in strs:
            key=''.join(sorted(i))
            if key not in anagram:
                anagram[key]=[]
            anagram[key].append(i)
        result=list(anagram.values())
        return result
        