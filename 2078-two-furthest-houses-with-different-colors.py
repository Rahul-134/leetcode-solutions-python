from typing import List

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        i, j = 0, len(colors) - 1
        max_distance = []
        while i<=(len(colors)-1)/2:
            if colors[i] != colors[j]:
                max_distance.append(abs(i-j))
            if i == j:
                i += 1
                j = len(colors) - 1
            else:
                j -= 1
        return max(max_distance)

c = Solution()
print(c.maxDistance([4,4,4,11,4,4,11,4,4,4,4,4]))