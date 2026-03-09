class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == "0" and b == "0":
            return "0"
        n1, n2 = 0, 0
        a, b = a[::-1], b[::-1]
        for i in range(len(a)):
            n1 += ((int(a[i])) * (2 ** i))
        for i in range(len(b)):
            n2 += ((int(b[i])) * (2 ** i))
        result = n1 + n2
        s = ""
        while result > 0:
            s += str(result%2)
            result = result // 2
        return s[::-1]

        # Alternate solution:
        # a1 = int(a,2)
        # a2 = int(b,2)
        # return bin(a1+a2)[2:]


c = Solution()
print(c.addBinary("0", "0"))