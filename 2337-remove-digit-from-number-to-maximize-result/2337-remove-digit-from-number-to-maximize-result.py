class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        count=""
        for i in range(len(number)):
            string=""
            if number[i]==digit:
                string=number[:i]+number[i+1:]
                if string > count :
                    count=string
        return count