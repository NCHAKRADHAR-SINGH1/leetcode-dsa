class Solution:
    def balancedStringSplit(self, s: str) -> int:
        number=0
        count=0
        for i  in s:
            if i=='R':
                number=number+1
            else:
                number=number-1
            if number==0:
                count=count+1

        return count