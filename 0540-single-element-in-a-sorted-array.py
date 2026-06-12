from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        i, j = 0, 1
        while j < len(nums):
            if nums[i] == nums[j]:
                i += 2
                j += 2
            else:
                return nums[i]
        return nums[-1]

c = Solution()
print(c.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))