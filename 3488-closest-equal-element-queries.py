from typing import List
from collections import defaultdict
import bisect

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # l = []
        # for i in queries:
        #     a = list(np.where(np.array(nums) == nums[i]))
        #     d = []
        #     for j in a[0]:
        #         d.append(abs(i-j))
        #         d.append(len(nums) - abs(i-j))
        #     if nums.count(nums[i]) <= 1:
        #         l.append(-1)
        #         continue
        #     l.append(int(sorted(d)[1]))
        # return l

        n = len(nums)
        val_to_indices = defaultdict(list)
        for idx, val in enumerate(nums):
            val_to_indices[val].append(idx)

        l = []
        for i in queries:
            indices = val_to_indices[nums[i]]

            if len(indices) <= 1:
                l.append(-1)
                continue

            idx_in_list = bisect.bisect_left(indices, i)

            prev_idx = indices[(idx_in_list - 1) % len(indices)]
            next_idx = indices[(idx_in_list + 1) % len(indices)]

            dist1 = abs(i - prev_idx)
            dist1 = min(dist1, n - dist1)

            dist2 = abs(i - next_idx)
            dist2 = min(dist2, n - dist2)

            l.append(int(min(dist1, dist2)))

        return l

c = Solution()
print(c.solveQueries([1,3,1,4,1,3,2], [0,3,5]))