class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        a = []
        for i in s:
            new_s = s[-1] + s[0:len(s)-1]
            a.append(new_s)
            s = new_s
        if goal in a:
            return True
        return False

c = Solution()
print(c.rotateString("abcde", "cdeab"))