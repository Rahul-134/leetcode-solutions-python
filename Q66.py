# Q66. Plus One
from typing import List
import numpy as np

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for i in digits:
            s += str(i)
        i = int(s) + 1
        s1 = str(i)
        a = []
        for i in s1:
            a.append(int(i))
        return a
c = Solution()
print(c.plusOne([9,9]))