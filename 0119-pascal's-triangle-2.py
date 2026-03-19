from typing import List
import numpy as np

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = []
        for i in range(rowIndex+1):
            a = []
            for j in range(i+1):
                a.append(1)
            result.append(a)

        for i in range(2,rowIndex+1):
            for j in range(1, i):
                result[i][j] = sum(result[i-1][j-1:j+1])

        return result[rowIndex]

c = Solution()
print(c.getRow(3))