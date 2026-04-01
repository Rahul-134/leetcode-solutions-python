from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        for i, j in enumerate(nums):
            if j > target:
                return i
        else:
            return len(nums)

c = Solution()
print(c.searchInsert([1,3,5,6], 7))