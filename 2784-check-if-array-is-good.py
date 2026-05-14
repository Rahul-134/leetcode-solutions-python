from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        a = []
        for i in range(1, n):
            a.append(i)
        a.append(n)
        a.append(n)
        return True if sorted(nums) == a else False

c = Solution()
print(c.isGood([2,1,3]))