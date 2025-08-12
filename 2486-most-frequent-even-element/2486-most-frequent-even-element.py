class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
           even=[ ch for ch in nums if ch %2==0]
           if all(ch%2 !=0 for ch in nums):
            return -1
           dici=Counter(even)
           max_element=max(dici.values())
           li=[ ch for ch  in even   if dici[ch]==max_element  ]
           return min(li)