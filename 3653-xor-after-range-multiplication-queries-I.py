from typing import List
import numpy as np
from functools import reduce

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        nums = np.array(nums)
        for i in queries:
            nums[i[0:3][0]: i[0:3][1] + 1: i[0:3][2]] = (nums[i[0:3][0]: i[0:3][1] + 1: i[0:3][2]] * i[-1]) % (10 ** 9 + 7)
        i = reduce(lambda x, y: x ^ y, nums)
        return int(i)

c = Solution()
print(c.xorAfterQueries([780], [[0,0,1,13],[0,0,1,17],[0,0,1,9],[0,0,1,18],[0,0,1,16],[0,0,1,6],[0,0,1,4],[0,0,1,11],[0,0,1,7],[0,0,1,18],[0,0,1,8],[0,0,1,15],[0,0,1,12]]))