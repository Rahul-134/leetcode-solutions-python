from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        nums.sort()
        for i in nums:
            if i not in d.keys():
                d.setdefault(i, nums.count(i))
        sorted_d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        ans = []
        for i in range(k):
            ans.append(list(sorted_d.keys())[i])
        return ans

c = Solution()
print(c.topKFrequent([1, 1, 1, 2, 2, 3], 2))