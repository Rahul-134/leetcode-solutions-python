from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a = [i for i, value in enumerate(nums) if value == target]
        if len(a) == 1:
            return a + a
        elif len(a) > 1:
            return [a[0], a[-1]]
        return [-1, -1]

c = Solution()
print(c.searchRange([5, 7, 7, 8, 8, 10], 8))