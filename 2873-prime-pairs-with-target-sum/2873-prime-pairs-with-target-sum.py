class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        if n <=1:
            return []
        is_prime=[True]*(n+1)
        is_prime[0]=is_prime[1]=False
        for i in range(2,int(n**0.5)+1):
            if is_prime[i]:
                for j in range(i*i,n+1,i):
                    is_prime[j]=False
        li=[]
        for x in range(2,n//2+1):
            y=n-x
            if is_prime[x] and is_prime[y]:
                li.append([x,y])
        return li
