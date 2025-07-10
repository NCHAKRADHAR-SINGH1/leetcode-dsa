class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dici=Counter(nums)
        heap=[]
        for num,freq in dici.items():
            heapq.heappush(heap,(freq,num))
            if len(heap)>k:
                heapq.heappop(heap)
        return [num for freq,num in sorted(heap,reverse=True)]
