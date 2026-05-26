class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0
        for i in set(word):
            if chr(ord(i) - 32) in word:
                count += 1
        return count

c = Solution()
print(c.numberOfSpecialChars("aaAbcBC"))