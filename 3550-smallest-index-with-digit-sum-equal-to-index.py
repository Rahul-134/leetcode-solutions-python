from typing import List

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for index, value in enumerate(nums):
            s = list(str(value))
            a = sum([int(i) for i in s])
            if index == a:
                return index
        return -1

c = Solution()
print(c.smallestIndex([1, 10, 11]))