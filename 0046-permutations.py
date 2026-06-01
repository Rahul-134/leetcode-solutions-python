from typing import List
import itertools

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        p = itertools.permutations(nums)
        a = [list(t) for t in p]
        return a

c = Solution()
print(c.permute([1, 2, 3]))