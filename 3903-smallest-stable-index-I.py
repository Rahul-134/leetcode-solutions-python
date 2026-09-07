class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        i, j = 0, len(nums)-1
        a = max(nums[0:i+1])
        b = min(nums[i:j+1])
        while a - b > k:
            i += 1
            if i>j:
                return -1
            a = max(nums[0:i+1])
            b = min(nums[i:j+1])
        return i

c = Solution()
print(c.firstStableIndex([5, 0, 1, 4], 3))