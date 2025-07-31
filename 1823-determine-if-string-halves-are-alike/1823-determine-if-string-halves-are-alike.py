class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        string1=""
        string2=""
        n=len(s)
        first_half=s[0:n//2]
        second_half=s[n//2:n]
        vowels={'a','e','i','o','u','A','E','I','O','U'}
        for ch in first_half:
            if ch in vowels:
                string1=string1+ch
        for ch in second_half:
            if ch in vowels:
                string2=string2+ch
        dici1=Counter(string1)
        dici2=Counter(string2)
        return sum(dici1.values())==sum(dici2.values())