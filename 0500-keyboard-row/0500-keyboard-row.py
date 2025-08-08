class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row={'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
        second_row={'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
        third_row={'z', 'x', 'c', 'v', 'b', 'n', 'm'}
        res=[]
        for i in range(len(words)):
            word=words[i]
            if all(ch in first_row for ch in word.lower()):
                res.append(word)
            elif all(ch in second_row for ch in word.lower()):
                res.append(word)
            elif all(ch in third_row for ch in word.lower()):
                 res.append(word)
            else:
                continue
        return (res)