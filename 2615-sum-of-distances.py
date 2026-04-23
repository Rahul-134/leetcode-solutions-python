from typing import List

class Solution:
    def distance(self, nums: List[int]) -> List[int]:

        # My solution:  O(n^2) time complexity

        # i, j = 0, len(nums) - 1
        # s = 0
        # l = []
        # while i < len(nums):
        #     while j >= 0:
        #         if nums[i] == nums[j]:
        #             s += abs(i - j)
        #         j -= 1
        #     l.append(s)
        #     s, j = 0, len(nums) - 1
        #     i += 1
        # return l

        # Optimised for O(n) time complexity
        n = len(nums)
        res = [0] * n

        count = {}
        total_idx_sum = {}

        for i, x in enumerate(nums):
            if x in count:
                res[i] += count[x] * i - total_idx_sum[x]
                count[x] += 1
                total_idx_sum[x] += i
            else:
                count[x] = 1
                total_idx_sum[x] = i

        count.clear()
        total_idx_sum.clear()

        for i in range(n - 1, -1, -1):
            x = nums[i]
            if x in count:
                res[i] += total_idx_sum[x] - count[x] * i
                count[x] += 1
                total_idx_sum[x] += i
            else:
                count[x] = 1
                total_idx_sum[x] = i

        return res

c = Solution()
print(c.distance([1, 3, 1, 1, 2]))