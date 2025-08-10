class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1=set(nums1)
        set2=set(nums2)
        return [sum( x in nums2 for x in nums1 ),sum(x in nums1  for x in nums2)]