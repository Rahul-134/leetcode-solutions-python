from typing import List

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mi, mx = nums[0], nums[0]
        for i in nums:
            if i<mi:
                mi = i
            if i>mx:
                mx = i
        g = 1
        for i in range(1, mi+1):
            if (mi % i == 0) and (mx % i == 0):
                if i > g:
                    g = i

        return g

        # one-liner solution:
        # import math
        # return math.gcd(min(nums), max(nums))

c = Solution()
print(c.findGCD([2, 5, 6, 9, 10]))