# 58. Length of Last Word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])

c = Solution()
print(c.lengthOfLastWord("luffy is still joyboy"))