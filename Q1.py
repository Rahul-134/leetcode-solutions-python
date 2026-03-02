# Two Sum
from typing import List

from sqlalchemy.util.langhelpers import repr_tuple_names
from tenacity import retry_unless_exception_type

import numpy as np
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = np.array(nums)
        for index, value in enumerate(nums):
            for j in nums[index+1::]:
                if j + value == target:
                    return [index, nums[index+1:].index(j) + index + 1]


c = Solution()
print(c.twoSum([2,7,11,15], 9))