class Solution:
    def reverseVowels(self, s: str) -> str:
        vow = []
        for i in s:
            if i in "aeiouAEIOU":
                vow.append(i)
        word = ""
        for i in s:
            if i not in "aeiouAEIOU":
                word += i
            else:
                word += vow.pop()
        return word

c = Solution()
print(c.reverseVowels("leetcode"))