from functools import reduce
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Brute force approach
        a = []
        rem = []
        i, n = 0, len(nums)
        while i<n:
            s = nums.pop(0)
            rem.append(s)
            a.append(reduce(lambda x, y: x*y, nums+rem[:len(rem)-1]))
            n -= 1
        return a

        # O(n) time complexity using prefix, suffix product
        # n = len(nums)
        # a = [1] * n
        #
        # prefix = 1
        # for i in range(n):
        #     a[i] = prefix
        #     prefix *= nums[i]
        #
        # suffix = 1
        # for i in range(n - 1, -1, -1):
        #     a[i] *= suffix
        #     suffix *= nums[i]
        #
        # return a

c = Solution()
print(c.productExceptSelf([1, 2, 3, 4]))