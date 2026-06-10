from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i, j = 0, 1
        nums.sort()
        while i<len(nums):
            if nums[i] ^ nums[j] == 0:
                return nums[i]
            i += 1
            j += 1

c = Solution()
print(c.findDuplicate([1, 3, 4, 2, 2]))