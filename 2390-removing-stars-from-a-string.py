class Solution:
    def removeStars(self, s: str) -> str:
        a = []
        for i in s:
            if i != "*":
                a.append(i)
            elif i == "*":
                a.pop()
        return "".join(a)

c = Solution()
print(c.removeStars("leet**cod*e"))