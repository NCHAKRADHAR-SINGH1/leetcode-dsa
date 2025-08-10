class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arr_set = set(arr)
        li = []
        for i in range(1, 50000):  # just needs to be high enough
            if i not in arr_set:
                li.append(i)
                if len(li) == k:
                    return li[-1]
