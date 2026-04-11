
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        s = self.countAndSay(n - 1)
        count = 1
        res = []
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                res.append(str(count))
                res.append(s[i - 1])
                count = 1
        res.append(str(count))
        res.append(s[-1])
        return "".join(res)

c = Solution()
print(c.countAndSay(6))