class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        count=""
        for index,value in enumerate(number):
            string=""
            if value==digit:
                string=number[:index]+number[index+1:]
                if string > count :
                    count=string
        return count