# 8. String to Integer (atoi)
import numpy as np
from numpy.ma.core import arange


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        sign = 1
        if s[0] in ['+', '-']:
            if s[0] == '-':
                sign = -1
            s = s[1:]

        result = 0
        for char in s:
            if char.isdigit():
                result = result * 10 + int(char)
            else:
                break

        result *= sign
        return max(min(result, 2**31 - 1), -2**31)
c = Solution()
print(c.myAtoi("-91283472332"))