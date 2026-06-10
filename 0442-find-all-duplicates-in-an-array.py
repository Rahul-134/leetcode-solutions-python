from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i, j = 0, 1
        nums.sort()
        a = []
        while j<len(nums):
            if nums[i] == nums[j]:
                a.append(nums[i])
            i += 1
            j += 1
        return list(set(a))

c = Solution()
print(c.findDuplicates([4,3,2,7,8,2,3,1]))