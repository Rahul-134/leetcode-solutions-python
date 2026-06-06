from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        right, left = [], []
        for i in range(len(nums)):
            left.append(sum(nums[:i]))
        for i in range(len(nums)):
            right.append(sum(nums[i+1:]))
        res = []
        for i in range(len(nums)):
            res.append(abs(right[i] - left[i]))
        return res

c = Solution()
print(c.leftRightDifference([10, 4, 8, 3]))