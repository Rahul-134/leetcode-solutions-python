import math
class Solution:
    def climbStairs(self, n: int) -> int:
        count = 1
        count_of_2 = 0
        n_copy = n
        if n % 2 == 1:
            while n > 1:
                n = n - 2
                count_of_2 += 1
        else:
            while n != 0:
                n -= 2
                count_of_2 += 1
        for i in range(1, count_of_2+1):
            r = n_copy-i*2
            count += ((math.factorial(i+r)) / (math.factorial(i)*math.factorial(r)))
        return int(count)
c = Solution()
print(c.climbStairs(5))