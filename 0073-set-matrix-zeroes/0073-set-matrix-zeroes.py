class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
      m=len(matrix)
      n=len(matrix[0])
      rows=[-1]*m
      cols=[-1]*n
      for i in range(m):
        for j in range(n):
            if matrix[i][j]==0:
                rows[i]=0
                cols[j]=0
      for i in range(m):
        for j in range(n):
            if rows[i]==0 or cols[j]==0:
                matrix[i][j]=0
        