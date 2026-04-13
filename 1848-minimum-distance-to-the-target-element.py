from typing import List
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        return min(abs(i-start) for i, j in enumerate(nums) if j == target)

c = Solution()
print(c.getMinDistance([1,1,1,1,1,1,1,1,1,1,1], 1, 9))