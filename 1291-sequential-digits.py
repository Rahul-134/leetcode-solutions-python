from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        a, s, adder = [], "", ""
        for i in range(1, len(str(low)) + 1):
            s += str(i)
            adder += "1"
        while int(s) <= high:
            a.append(int(s))
            s, adder = new_s(s, adder)
        return [i for i in a if i >= low]


def new_s(s, adder):
    if s[-1] == "9":
        a = ""
        adder += "1"
        for j in range(1, len(s) + 1):
            a += str(j)
        return a + str(int(a[-1]) + 1), adder
    return str(int(s) + int(adder)), adder

c = Solution()
print(c.sequentialDigits(58, 155))