from typing import List
import pandas as pd


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # df = pd.DataFrame(nums)
        # return df.value_counts().index[-1][0]
        d = {}
        for i in nums:
            if i not in d:
                d.setdefault(i, nums.count(i))
        for key, value in d.items():
            if value == 1:
                return key
        # 0ms time complexity
        # result = 0
        # for num in nums:
        #     result ^= num
        # return result

c = Solution()
print(c.singleNumber([4,1,2,1,2]))