from typing import List

import math
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        a = []
        for i in range(1, n+1):
            for j in range(1, i):
                if math.gcd(i, j) == 1:
                    a.append(str(j) + "/" + str(i))
        return a

c = Solution()
print(c.simplifiedFractions(4))