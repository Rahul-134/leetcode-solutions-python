# Q50. Pow(x, n)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x<=1 or x>0:
            return x ** n
        if (n < -100) and (x>-1 and x<1):
            return 0.0
        if x == -1:
            return -1 if n%2 == 1 else 1
        if n>0:
            c = x
            for i in range(n-1):
                x = c * x
        elif n == 0:
            return 1
        elif n<0:
            x = 1/x
            c = x
            for i in range((n*-1) - 1):
                x = c * x
        return x
c = Solution()
print(c.myPow(-1, -2147483648))