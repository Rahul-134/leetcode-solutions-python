from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count, s = 0, 0
        if sum(costs) <= coins:
            return len(costs)
        for i in sorted(costs):
            if i <= coins:
                if s+i <= coins:
                    count += 1
                    s += i
        return count

c = Solution()
print(c.maxIceCream([1, 3, 2, 4, 1], 7))