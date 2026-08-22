class Solution:
    def checkDivisibility(self, n: int) -> bool:
        l = [int(i) for i in str(n)]
        s = sum(l)
        m = 1
        for i in l:
            m *= i
        return n % (s+m) == 0

c = Solution()
print(c.checkDivisibility(99))