class Solution:
    def isHappy(self, n: int) -> bool:
        def happynumber(n):
            seen=set()
            while n!=1 and n not in seen:
                total=0
                seen.add(n)
                while n >0:
                    digit=n % 10
                    total=total+digit*digit
                    n=n //10
                n=total
            return n==1
        return happynumber(n)

