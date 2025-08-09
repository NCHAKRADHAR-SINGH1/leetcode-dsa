class Solution:
    def secondHighest(self, s: str) -> int:
        seen=set([int(i) for i in s if i.isdigit()])
        li=list((seen)) 
        if len(li) < 2:
            return -1
        k=1
        heap=[]
        for i in li:
            heapq.heappush(heap,-i) #[-3,-2,-1],the heappush contains the first element with smallest ,remaining unorder
        if len(li) >= 2:
            for i in range(k):
                heapq.heappop(heap)#[-3],it removes the smallest ,After heapq.heappop(heap):
                                   #Removes -3 (smallest value, i.e. largest positive number 3).

                                   #Python now needs to reheapify to keep the smallest element at index 0.

                                   #Between -1 and -2, the smallest is -2, so it becomes the new root.
        return (-heap[0]) 

         
      