# 9. Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)==str(x)[::-1]

c = Solution()
print(c.isPalindrome(10))