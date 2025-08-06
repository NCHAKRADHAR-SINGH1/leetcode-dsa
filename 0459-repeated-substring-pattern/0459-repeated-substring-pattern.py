class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        doubled=s+s
        remain_string=doubled[1:-1]
        return s in remain_string 