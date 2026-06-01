class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for i in s:
            d.setdefault(i, s.count(i))
        sorted_dict = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        t = ""
        for i, j in sorted_dict.items():
            t += i*j
        return t

c = Solution()
print(c.frequencySort("tree"))