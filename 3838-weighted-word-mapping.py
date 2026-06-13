from typing import List

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        d = {
            "z": 0, "y": 1, "x": 2, "w": 3, "v": 4, "u": 5, "t": 6, "s": 7, "r": 8, "q": 9, "p": 10,
            "o": 11, "n": 12, "m": 13, "l": 14, "k": 15, "j": 16, "i": 17, "h": 18, "g": 19, "f": 20,
            "e": 21, "d": 22, "c": 23, "b": 24, "a": 25,
        }
        a = []
        word = ""
        weights.reverse()
        for i in words:
            s = 0
            for j in i:
                s += weights[d.get(j)]
            a.append(s % 26)
        for i in a:
            for j, k in d.items():
                if i == k:
                    word += j
        return word

c = Solution()
print(c.mapWordWeights(["abcd","def","xyz"], [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]))