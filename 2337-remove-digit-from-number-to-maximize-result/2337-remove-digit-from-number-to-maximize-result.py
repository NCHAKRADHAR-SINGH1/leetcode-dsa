class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        count=""
        for ch,value in enumerate(number):
            string=""
            if value==digit:
                string=number[:ch]+number[ch+1:]
                if string > count :
                    count=string
        return count