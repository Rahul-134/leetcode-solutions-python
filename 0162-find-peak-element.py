from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return nums.index(max(nums))

c = Solution()
print(c.findPeakElement([1,2,1,3,5,6,4]))