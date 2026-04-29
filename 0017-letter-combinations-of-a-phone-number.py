from typing import List
from itertools import combinations

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        a = []
        if len(digits) == 1:
            return list(d.get(digits))
        elif len(digits) == 2:
            i, j = 0, 0
            l = [d.get(i) for i in digits]
            while i < len(d.get(digits[0])):
                while j < len(d.get(digits[1])):
                    a.append(l[0][i] + l[1][j])
                    j += 1
                i+=1
                j = 0
        elif len(digits) == 3:
            i, j, k = 0, 0, 0
            l = [d.get(i) for i in digits]
            while i < len(d.get(digits[0])):
                while j < len(d.get(digits[1])):
                    while k < len(d.get(digits[2])):
                        a.append(l[0][i] + l[1][j] + l[2][k])
                        k += 1
                    j += 1
                    k = 0
                i += 1
                j = 0
        elif len(digits) == 4:
            i, j, k, m = 0, 0, 0, 0
            l = [d.get(i) for i in digits]
            while i < len(d.get(digits[0])):
                while j < len(d.get(digits[1])):
                    while k < len(d.get(digits[2])):
                        while m < len(d.get(digits[3])):
                            a.append(l[0][i] + l[1][j] + l[2][k] + l[3][m])
                            m += 1
                        k += 1
                        m = 0
                    j += 1
                    k = 0
                i += 1
                j = 0
        return a

c = Solution()
print(c.letterCombinations("23"))