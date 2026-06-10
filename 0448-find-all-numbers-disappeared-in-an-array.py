from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        return [i for i in range(1, len(nums)+1) if i not in nums_set]

c = Solution()
print(c.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))