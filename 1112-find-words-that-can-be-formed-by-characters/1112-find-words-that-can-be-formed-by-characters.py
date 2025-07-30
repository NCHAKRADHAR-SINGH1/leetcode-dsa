class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total_count=0
        dici1=Counter(chars)
        for i in range(len(words)):
            word=Counter(words[i])
            if all(word[ch] <= dici1.get(ch,0) for ch in word):
                total_count=total_count+len(words[i])
        return total_count
