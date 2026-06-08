from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        more = []
        count = 0
        for i in nums:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                count += 1
        nums.clear()
        for i in less:
            nums.append(i)
        for i in range(count):
            nums.append(pivot)
        for i in more:
            nums.append(i)
        return nums

c = Solution()
print(c.pivotArray([9, 12, 5, 10, 14, 3, 10], 10))