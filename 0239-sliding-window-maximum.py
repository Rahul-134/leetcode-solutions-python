from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        l = range(0, len(nums) - k + 1)
        return  [max(nums[i:k+i]) for i in l]

        # Least possible time complexity:
        # if not nums:
        #     return []
        # result = []
        # q = deque()
        # for i in range(len(nums)):
        #     while q and nums[q[-1]] < nums[i]:
        #         q.pop()
        #     q.append(i)
        #     if q[0] == i - k:
        #         q.popleft()
        #     if i >= k - 1:
        #         result.append(nums[q[0]])
        # return result

c = Solution()
print(c.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))