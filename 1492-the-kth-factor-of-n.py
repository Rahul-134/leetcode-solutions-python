class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        a = [i for i in range(1, n+1) if n%i==0]
        return a[k-1] if len(a) >= k else -1

c = Solution()
print(c.kthFactor(12, 3))