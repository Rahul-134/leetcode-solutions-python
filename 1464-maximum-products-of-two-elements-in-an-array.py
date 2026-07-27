from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a = [i-1 for i in nums]
        a.sort()
        return a[-1] * a[-2]

        # One-liner solution:
        # return (sorted(nums)[-1] - 1) * (sorted(nums)[-2] - 1)

c = Solution()
print(c.maxProduct([1, 5, 4, 5]))