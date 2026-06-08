from typing import List

class Solution:
    def printVertically(self, s: str) -> List[str]:
        l = [list(a) for a in s.split()]
        max_length = max([len(k) for k in l])
        i = 0
        sent = []
        while i < max_length:
            a = ""
            for j in l:
                if i<len(j):
                    a += j[i]
                else:
                    a += " "
            sent.append(a.rstrip())
            i += 1
        return sent

c = Solution()
print(c.printVertically("TO BE OR NOT TO BE"))