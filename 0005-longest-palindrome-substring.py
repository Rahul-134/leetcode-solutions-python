class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s[::-1] == s:
            return s
        result = []
        for index, value in enumerate(s):
            for i, j in enumerate(s):
                a = s[index:len(s)-i]
                a_rev = a[::-1]
                if a == a_rev:
                    result.append(a)
        print(result)
        return max(result, key=len)


c = Solution()
print(c.longestPalindrome("babad"))