class Solution:
    def reverseDegree(self, s: str) -> int:
        result = 0
        for index, value in enumerate(s):
            a = (26-(ord(value) - 97)) * (index+1)
            result += a
        return result

c = Solution()
print(c.reverseDegree("zaza"))