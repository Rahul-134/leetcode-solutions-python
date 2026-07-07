class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
        s = "".join(str(n).split("0"))
        l = [int(i) for i in s]
        return sum(l) * int(s)


        # One-liner :
        # return sum([int(i) for i in "".join(str(n).split("0"))]) * int("".join(str(n).split("0"))) if n>0 else 0

c = Solution()
print(c.sumAndMultiply(10203004))