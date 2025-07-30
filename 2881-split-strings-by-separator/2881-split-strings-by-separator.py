class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        remain_word=""
        for word in words :
            cleaned=word.replace(separator," ")
            remain_word=remain_word+" "+cleaned
        return (remain_word.split())