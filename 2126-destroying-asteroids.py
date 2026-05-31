from typing import List

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        i, j = 0, 1
        asteroids.sort()
        flag = True
        if mass < asteroids[0]:
            return False
        while j<len(asteroids):
            mass += asteroids[i]
            if mass < asteroids[j]:
                flag = False
                break
            i += 1
            j += 1
        return flag

c = Solution()
print(c.asteroidsDestroyed(10, [3, 9, 19, 5, 21]))