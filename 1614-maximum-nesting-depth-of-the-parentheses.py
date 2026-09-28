class Solution:
    def maxDepth(self, s: str) -> int:
        a = []
        max_length = 0
        for i in s:
            if i == "(":
                a.append(i)
            elif i == ")":
                a.pop()
            if max_length < len(a):
                max_length = len(a)
        return max_length

c = Solution()
print(c.maxDepth("(1+(2*3)+((8)/4))+1"))