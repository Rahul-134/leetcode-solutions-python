from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # my approach: O(n^2) time complexity

        keys = []
        for i in strs:
            val = "".join(sorted(i))
            if val not in keys:
                keys.append(val)

        lookup = {key: [] for key in keys}

        for j in strs:
            sorted_j = "".join(sorted(j))
            lookup[sorted_j].append(j)

        ans = []
        for i in keys:
            ans.append(lookup[i])

        return ans

        # O(n) solution:

        # db = defaultdict(list)
        #
        # for s in strs:
        #     key = tuple(sorted(s))
        #     db[key].append(s)
        #
        # return list(db.values())

c = Solution()
print(c.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))