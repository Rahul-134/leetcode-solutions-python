from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        a = [i.count("1") for i in bank]
        mul = []
        i, j = 0, 1
        # print(a)
        while i<len(a):
            while j<len(a):
                if a[j] == 0:
                    j += 1
                    continue
                mul.append(a[i]*a[j])
                break
            i += 1
            j = i+1
        # print(mul)
        return sum(mul)

c = Solution()
print(c.numberOfBeams(["011001","000000","010100","001000"]))