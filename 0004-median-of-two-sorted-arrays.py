from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = sorted(nums1 + nums2)
        return l[len(l) // 2] if len(l)%2==1 else (l[len(l) // 2] + l[(len(l) // 2) - 1]) / 2

c = Solution()
print(c.findMedianSortedArrays([1,2], [3,4]))