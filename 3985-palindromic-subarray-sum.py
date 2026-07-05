from typing import List

class Solution:
    def getSum(self, nums: List[int]) -> int:
        if nums == nums[::-1]:
            return sum(nums)
        a = []
        i, j = 0, 1
        while i < len(nums):
            while j < len(nums):
                if nums[i:j] == nums[i:j][::-1]:
                    a.append(sum(nums[i:j]))
                j += 1
            i += 1
            j = i+1
        i, j = 0, 1
        nums.reverse()
        while i < len(nums):
            while j < len(nums):
                if nums[i:j] == nums[i:j][::-1]:
                    a.append(sum(nums[i:j]))
                j += 1
            i += 1
            j = i+1
        return max(a) if len(a) > 0 else 0

        # O(n) solution:

        # if not nums:
        #     return 0
        # T = []
        # for x in nums:
        #     T.extend(['#', x])
        # T.append('#')
        #
        # n = len(T)
        # P = [0] * n
        # C = R = 0
        #
        # prefix = [0] * (len(nums) + 1)
        # for i in range(len(nums)):
        #     prefix[i + 1] = prefix[i] + nums[i]
        #
        # max_sum = 0
        #
        # for i in range(n):
        #     mirror = 2 * C - i
        #     if i < R:
        #         P[i] = min(R - i, P[mirror])
        #
        #     while i - 1 - P[i] >= 0 and i + 1 + P[i] < n and T[i - 1 - P[i]] == T[i + 1 + P[i]]:
        #         P[i] += 1
        #
        #     if i + P[i] > R:
        #         C = i
        #         R = i + P[i]
        #
        #     start_idx = (i - P[i]) // 2
        #     end_idx = (i + P[i]) // 2 - 1
        #
        #     if start_idx <= end_idx:
        #         current_sum = prefix[end_idx + 1] - prefix[start_idx]
        #         max_sum = max(max_sum, current_sum)
        #
        # return max_sum

c = Solution()
print(c.getSum([7, 1, 2, 1, 7, 3, 4, 3, 4]))