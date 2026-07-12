from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        d, r = {}, 1
        for i, j in enumerate(sorted(arr)):
            if j in d.keys():
                continue
            d.setdefault(j, r)
            r += 1
        rank = []
        for i in arr:
            rank.append(d[i])
        return rank

c = Solution()
print(c.arrayRankTransform([37,12,28,9,100,56,80,5,12]))