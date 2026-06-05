from typing import List

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        a = []
        l_s1, l_s2 = s1.split(), s2.split()
        d = {}
        for i in l_s1:
            d.setdefault(i, l_s1.count(i) + l_s2.count(i))
        for i in l_s2:
            d.setdefault(i, l_s1.count(i) + l_s2.count(i))
        for i, j in d.items():
            if j == 1:
                a.append(i)
        return a

c = Solution()
print(c.uncommonFromSentences("this apple is sweet", "this apple is sour"))