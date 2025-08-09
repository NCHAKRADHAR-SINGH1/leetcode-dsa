class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        unique_words=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        seen=set()
        dici={}
        for i in range(len(unique_words)):
            dici[alphabets[i]]=unique_words[i]
        for i in range(len(words)):
            t=""
            for ch in words[i]:
               t=t+dici[ch]
            seen.add(t)
        return len(seen)