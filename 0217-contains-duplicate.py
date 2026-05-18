from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return not len(nums) == len(set(nums))

c = Solution()
print(c.containsDuplicate([1, 2, 3, 1]))