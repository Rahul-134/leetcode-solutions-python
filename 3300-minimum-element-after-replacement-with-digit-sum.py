from typing import List

class Solution:
    def minElement(self, nums: List[int]) -> int:
        a = []
        for i in nums:
            l = list(int(k) for k in list(str(i)))
            a.append(sum(l))
        return min(a)

c = Solution()
print(c.minElement([10, 12, 13, 14]))