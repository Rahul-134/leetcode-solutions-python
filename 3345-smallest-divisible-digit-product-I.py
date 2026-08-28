class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        l = [int(i) for i in str(n)]
        mul = 1
        for i in l:
            mul *= i
        if mul % t == 0:
            return n
        return self.smallestNumber(n+1, t)

c = Solution()
print(c.smallestNumber(15, 3))