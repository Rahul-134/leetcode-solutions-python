# Two Sum
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, value in enumerate(nums):
            for j in nums[index+1::]:
                if j + value == target:
                    return [index, nums[index+1:].index(j) + index + 1]


c = Solution()
print(c.twoSum([0,5,11,7,15,2,2], 4))  # Change values and try running