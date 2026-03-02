# 8. String to Integer (atoi)
import numpy as np
from numpy.ma.core import arange


class Solution:
    def myAtoi(self, s: str) -> int:
        range = np.array(arange(-2147483648, 2147483648))
        result = "0"
        for i in s:
            if i.isdigit():
                result += i
            elif i == "-" and len(result) == 1:
                result += i
            elif i.isspace():
                continue
            else:
                break
        return 0 if len(result) == 1 else (range[0] if int(result[1:]) not in range else int(result[1:]))
c = Solution()
print(c.myAtoi("-91283472332"))