# Q7. Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        s = str(x)
        s1 = s[::-1] if x>0 else s[:0:-1]
        if int(s1) not in range(-2 ** 31, 2**31):
            return 0
        return int(s1) if x>0 else -1 * int(s1)

c = Solution()
print(c.reverse(1534236469))

# __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))