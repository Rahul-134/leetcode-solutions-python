from typing import List
import numpy as np
from itertools import combinations

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        d = {}
        distances = {}
        ans = []
        dummy = []
        if len(nums) < 3:
            return -1
        for i in nums:
            d.setdefault(i, nums.count(i))
        if max(d.values()) < 3:
            return -1
        print(d)
        nums = np.array(nums)
        ky = 1
        for key, value in d.items():
            if value >= 3:
                distances.setdefault(ky, np.where(nums == key))
                ky += 1
        for values in distances.values():
            dummy.append(list(combinations(values[0], 3)))
        for j in dummy:
            for i in j:
                ans.append(abs(i[0] - i[1]) + abs(i[1] - i[2]) + abs(i[0] - i[2]))
        return int(min(ans))


c = Solution()
print(c.minimumDistance([1,2,1,1,2,2]))