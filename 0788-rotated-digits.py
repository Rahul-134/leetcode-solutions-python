class Solution:
    def rotatedDigits(self, n: int) -> int:
        d = {
            "0": "0",
            "1": "1",
            "8": "8",
            "2": "5",
            "5": "2",
            "6": '9',
            '9': '6'
        }
        count = 0
        for i in range(1, n+1):
            a = str(i)
            s = ""
            for j in a:
                if j in d.keys():
                    s += d.get(j)
            if s != a and s != '' and len(s) == len(a):
                count += 1
        return count

c = Solution()
print(c.rotatedDigits(857))