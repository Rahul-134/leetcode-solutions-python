from typing import List

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
            # My solution:
            # n = ((i, k) for i, j in enumerate(nums1) for k, l in enumerate(nums2) if (i<=k) and (j<=l))
            # distance = list((i[1] - i[0]) for i in n)
            # return max(distance) if len(distance) > 0 else 0

            # Optimized for time complexity:
            i = j = max_dist = 0
            m, n = len(nums1), len(nums2)
            while i < m and j < n:
                if nums1[i] <= nums2[j]:
                    max_dist = max(max_dist, j - i)
                    j += 1
                else:
                    i += 1
                    if i > j:
                        j = i
            return max_dist
c = Solution()
print(c.maxDistance([55,30,5,4,2], [100,20,10,10,5]))