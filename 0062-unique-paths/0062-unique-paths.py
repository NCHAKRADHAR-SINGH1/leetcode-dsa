class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        li=[[0 for j in range(n)] for i in range(m)]
        for i in range(0,m):
            for j in range(0,n):
                if(i==0 or j==0):
                    li[i][j]=1
                else:
                    li[i][j]=li[i][j-1]+li[i-1][j]
        return li[m-1][n-1]
               
        