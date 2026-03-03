# 326 / 231 / 342 Power of Three / Two / Four
# Replace 3 by 2 and 4 respectively

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1

c = Solution()
print(c.isPowerOfThree(27))