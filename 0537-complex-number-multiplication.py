class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a = int(num1.split("+")[0])
        b = int(num1.split("+")[1][:-1])
        c = int(num2.split("+")[0])
        d = int(num2.split("+")[1][:-1])

        m = a*c - b*d
        n = a*d + b*c

        return str(m) + "+" + str(n) + "i"

c = Solution()
print(c.complexNumberMultiply("1+1i", "1+1i"))