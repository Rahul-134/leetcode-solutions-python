from typing import List

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        return (max(nums) - min(nums)) * k

c = Solution()
print(c.maxTotalValue([1, 3, 2], 2))