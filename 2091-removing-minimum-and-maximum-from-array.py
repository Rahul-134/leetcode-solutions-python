from typing import List

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1

        idx1 = nums.index(min(nums))
        idx2 = nums.index(max(nums))

        left, right = min(idx1, idx2), max(idx1, idx2)

        opt1 = right + 1

        opt2 = n - left

        opt3 = (left + 1) + (n - right)

        return min(opt1, opt2, opt3)

c = Solution()
print(c.minimumDeletions([0,-4,19,1,8,-2,-3,5]))