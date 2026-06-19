from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        a, j = [0], 0
        for i in gain:
            a.append(i + a[j])
            j += 1
        return max(a)

c = Solution()
print(c.largestAltitude([-5, 1, 5, 0, -7]))