from typing import List
import numpy as np

class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words:
            return -1
        if words[startIndex] == target:
            return 0
        l = list(np.where(np.array(words) == target))
        distance = []
        for i in l[0]:
            distance.append(abs(i-startIndex))
            distance.append(len(words) - abs(i-startIndex))
        return int(min(distance))


c = Solution()
print(c.closestTarget(["hello","i","am","leetcode","hello"], "hello", 1))