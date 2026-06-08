from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        i = 0
        tp = []
        while i<len((matrix[0])):
            a = []
            for j in matrix:
                a.append(j[i])
            tp.append(a)
            i+=1
        return tp

c = Solution()
print(c.transpose([[1,2,3],[4,5,6]]))