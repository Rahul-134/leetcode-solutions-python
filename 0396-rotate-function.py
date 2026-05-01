from typing import List
import numpy as np

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        # a = []
        # values = []
        # s = 0
        # for i, j in enumerate(nums):
        #     a = [nums[-1], *nums[0:len(nums) - 1]]
        #     nums = a
        #     for j, k in enumerate(a):
        #         s += k*j
        #     values.append(s)
        #     s = 0
        # return max(values)

        # O(n) time complexity
        n = len(nums)
        total_sum = sum(nums)

        current_weighted_sum = sum(i * val for i, val in enumerate(nums))
        max_val = current_weighted_sum

        for i in range(1, n):
            current_weighted_sum = current_weighted_sum + total_sum - n * nums[n - i]
            max_val = max(max_val, current_weighted_sum)

        return max_val

c = Solution()
print(c.maxRotateFunction([4,3,2,6]))