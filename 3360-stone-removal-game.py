class Solution:
    def canAliceWin(self, n: int) -> bool:
        prev = 10
        flag = 1
        while n >= prev:
            n -= prev
            prev -= 1
            flag *= -1
        return True if flag == -1 else False

c = Solution()
print(c.canAliceWin(12))