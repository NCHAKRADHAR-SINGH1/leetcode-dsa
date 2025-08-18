class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        li=[ i   for i in range(left,right+1,1)]
        res=[]
        for num in li:
            temp=num
            while temp > 0:
                digit=temp % 10
                if digit != 0 and num % digit ==0:
                    temp=temp//10
                else:
                    break
            else:
                res.append(num)
        return res