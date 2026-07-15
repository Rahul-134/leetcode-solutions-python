import math
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        even, odd = [], []
        e, o = 2, 1
        for i in range(n):
            even.append(e)
            odd.append(o)
            e += 2
            o += 2
        return math.gcd(sum(even), sum(odd))

        # f(x) = x;
        # return n

c = Solution()
print(c.gcdOfOddEvenSums(5))