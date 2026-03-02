# 344. Reverse String
from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i, j in enumerate(s):
            if i < (len(s) / 2):
                s[i], s[(i+1) * -1] = s[(i+1) * -1], s[i]
            else:
                break
        print(s)
c = Solution()
c.reverseString(["h","e","l","l","o"])