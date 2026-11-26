class Solution:
    def checkString(self, s: str) -> bool:
        return "".join(sorted(list(s))) == s

c = Solution()
print(c.checkString("aaabbb"))