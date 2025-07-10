class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
       heap=[]
       m=len(matrix)
       n=len(matrix[0])
       for i in range(m):
           for j in range(n):
              heap.append(matrix[i][j])
       min_heap=[]
       for num in heap:
            heapq.heappush(min_heap,-num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
       return (-min_heap[0])