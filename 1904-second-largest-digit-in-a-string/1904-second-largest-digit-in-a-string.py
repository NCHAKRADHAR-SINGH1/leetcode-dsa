class Solution:
    def secondHighest(self, s: str) -> int:
        seen=set([int(i) for i in s if i.isdigit()])
        li=list((seen)) 
        if len(li) < 2:
            return -1
        k=1
        heap=[]
        for i in li:
            heapq.heappush(heap,-i)
        if len(li) >= 2:
            for i in range(k):
                heapq.heappop(heap)
        return (-heap[0])

         
      