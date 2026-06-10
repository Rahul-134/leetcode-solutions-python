from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # One-liner:
        return [i for i in nums if nums.count(i) == 1][0]

        # d = {}
        # for i in nums:
        #     d.setdefault(i, nums.count(i))
        # for i, j in d.items():
        #     if j == 1:
        #         return i

c = Solution()
print(c.singleNumber([2, 2, 3, 2]))