from typing import List

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        a = [1 for i in patterns if i in word]
        return sum(a)

c = Solution()
print(c.numOfStrings(["a", "abc", "bc", "d"], "abc"))