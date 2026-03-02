# 125. Valid Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = "".join(list(filter(lambda x: x.lower().isalnum(), s)))
        return result.lower() == result[::-1].lower()

c = Solution()
print(c.isPalindrome("A man, a plan, a canal: Panama"))