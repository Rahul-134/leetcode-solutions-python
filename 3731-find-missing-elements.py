from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        a = []
        nums.sort()
        for i in range(nums[0], nums[-1]):
            if i not in nums:
                a.append(i)
        return a

c = Solution()
print(c.findMissingElements([5, 1]))