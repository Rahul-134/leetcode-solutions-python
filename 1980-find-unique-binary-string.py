from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        s = []
        n = len(nums)
        for i in range(0, 2**n):
            s.append(format(i, f'0{n}b'))
        a = [i for i in s if i not in nums]
        return a[0]


c = Solution()
print(c.findDifferentBinaryString(["1"]))