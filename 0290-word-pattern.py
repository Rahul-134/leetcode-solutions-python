# 290. Word Pattern

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        a = {}
        b = {}
        count = 0
        if pattern == s and len(s) > 1:
            return False
        for i, j in enumerate(pattern):
            if i < len(words):
                a.setdefault(j, words[i])
                b.setdefault(words[i], j)
        for i, j in enumerate(pattern):
            if i < len(words):
                if (a.get(j) == words[i]) and (b.get(words[i]) == j):
                    count += 1
        print(a, b, count)
        return True if len(pattern) == count and count == len(words) else False

c = Solution()
print(c.wordPattern("he", "unit"))