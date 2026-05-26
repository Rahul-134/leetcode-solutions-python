class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        c = []
        if n < int(str(n)[::-1]):
            for i in range(n, int(str(n)[::-1]) + 1):
                if is_prime_fast(i):
                    c.append(i)
        else:
            for i in range(int(str(n)[::-1]), n + 1):
                if is_prime_fast(i):
                    c.append(i)
        return sum(c)


def is_prime_fast(n):
    if n <= 1: return False
    if n <= 3: return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


c = Solution()
print(c.sumOfPrimesInRange(13))