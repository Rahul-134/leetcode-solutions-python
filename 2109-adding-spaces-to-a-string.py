from typing import List

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        a = ""
        temp = 0
        for i in spaces:
            a += s[temp:i] + " "
            temp = i
        a += s[spaces[-1]:]
        return a

c = Solution()
print(c.addSpaces("LeetcodeHelpsMeLearn", [8, 13, 15]))