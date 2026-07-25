class Solution:
    def maxProduct(self, n: int) -> int:
        l = [int(i) for i in str(n)]
        l.sort(reverse = True)
        return l[0] * l[1]

c = Solution()
print(c.maxProduct(124))