from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        a = []
        asc = sorted(nums)
        desc = asc[::-1]
        a.append(asc[0]*asc[1]*asc[2])
        a.append(desc[0]*desc[1]*desc[2])
        a.append(asc[0]*asc[1]*desc[0])
        a.append(desc[0]*desc[1]*asc[0])
        return max(a)

c = Solution()
print(c.maximumProduct([-3, -4, -5, -6]))