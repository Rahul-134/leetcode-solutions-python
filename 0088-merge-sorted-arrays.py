from typing import List
import numpy as np

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
            # nums1 = sorted(nums1[:m] + nums2)
            # print(nums1)

            i = m - 1
            j = n - 1
            k = m + n - 1
            while i >= 0 and j >= 0:
                if nums1[i] > nums2[j]:
                    nums1[k] = nums1[i]
                    i -= 1
                else:
                    nums1[k] = nums2[j]
                    j -= 1
                k -= 1
            while j >= 0:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1
            print(nums1)

c = Solution()
c.merge([1,2,3,0,0,0], 3, [2,5,6], 3)