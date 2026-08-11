from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        val = nums[0]
        j = 1
        total = val
        if len(nums) == 1:
            return nums[0] + 1
        while val + 1 == nums[j]:
            val = nums[j]
            total += val
            j += 1
            if j>=len(nums):
                break
        while total in nums:
            total += 1
        return total

c = Solution()
print(c.missingInteger([3,4,5,1,12,14,13]))