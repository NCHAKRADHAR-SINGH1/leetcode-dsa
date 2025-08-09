class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        result1 = []
        result2 = []
        for value in nums1:
            if value in nums2:
               continue
            elif value not in result1:
               result1.append(value)
        for value in nums2:
            if value in nums1:
               continue
            elif value not in result2:
               result2.append(value)
        return ([result1, result2])