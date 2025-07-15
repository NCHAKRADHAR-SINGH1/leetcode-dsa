class Solution:
    def isValid(self, word: str) -> bool:
        vowels={'a','e','i','o','u','A','E','I','O','U'}
        if len(word) < 3:
            return False
        is_vowel=False
        is_consonant=False
        for char in word:
            if not (char.isdigit() or char.isalpha()):
                 return False
            elif char in vowels:
                is_vowel=True
            elif char.isalpha():
                is_consonant=True
        return ( is_vowel and is_consonant)