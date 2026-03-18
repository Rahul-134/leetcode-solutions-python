from typing import List
import numpy as np

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            a = []
            for j in range(i+1):
                a.append(1)
            result.append(a)

        for i in range(2,numRows):
            for j in range(1, i):
                result[i][j] = sum(result[i-1][j-1:j+1])

        return result

c = Solution()
print(c.generate(5))