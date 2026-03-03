# Q41. First Missing Positive

from typing import List
import numpy as np
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # nums = np.array(nums)
        # i = 1
        # for n in nums:
        #     if i in nums:
        #         i += 1
        #     else:
        #         break
        # return i

        s = set(nums)
        for i in range(1, 10**5 + 2):
            if i not in s:
                return i

c = Solution
print(c.firstMissingPositive(self=Solution(), nums=[7,8,9,11,12]))