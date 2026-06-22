class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = {}
        count = 0
        a = [text.count(i) for i in set(text)]
        for i, j in enumerate(a):
            d.setdefault(list(set(text))[i], j)
        while d.get("b", 0) >= 1 and d.get("a", 0) >= 1 and d.get("l", 0) >= 2 and d.get("o", 0) >= 2 and d.get("n", 0) >= 1:
            count += 1
            d["b"] -= 1
            d["a"] -= 1
            d["l"] -= 2
            d["o"] -= 2
            d["n"] -= 1
        return count

c = Solution()
print(c.maxNumberOfBalloons("loonbalxballpoon"))