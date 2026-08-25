from typing import List

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        diff = k
        while k in nums:
            k += diff
        return k

c = Solution()
print(c.missingMultiple([8,2,3,4,6], 2))