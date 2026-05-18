from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == len(set(nums)):
            return False
        for i, j in enumerate(nums):
            if j in nums[i+1:i+k+1]:
                return True
        return False

c = Solution()
print(c.containsNearbyDuplicate([1,0,1,1], 1))