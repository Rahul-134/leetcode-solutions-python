# 27. Remove Element
from itertools import count
from typing import List
import numpy as np
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums = list(filter(lambda x: x != val, nums))
        print(list(nums))
        k = len(nums)
        return k
c = Solution()
print(c.removeElement([0,1,2,2,3,0,4,2], 2))