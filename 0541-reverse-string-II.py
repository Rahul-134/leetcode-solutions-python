class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = ""
        a = s
        for i in s:
            result += a[:k][::-1] + a[k:2*k]
            a = a[2 * k:]

        return result[:len(s)]

        # lesser time complexity:
        # s = list(s)
        #
        # for i in range(0, len(s), 2 * k):
        #     s[i:i + k] = reversed(s[i:i + k])
        #
        # return ''.join(s)



c = Solution()
print(c.reverseStr("abcdefg", 2))