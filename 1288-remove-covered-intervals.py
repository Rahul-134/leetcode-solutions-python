from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        i, j, count, a = 0, 1, 0, []
        while i < len(intervals):
            while j < len(intervals):
                if (intervals[j][0] >= intervals[i][0]) and (intervals[j][1] <= intervals[i][1]):
                    if intervals[j] not in a:
                        count += 1
                        a.append(intervals[j])
                j += 1
            i += 1
            j = i+1
        return len(intervals) - count

        # optimized solution O(n*logN) using a simple linear scan:
        # intervals.sort(key=lambda x: (x[0], -x[1]))
        #
        # count = 0
        # max_end = 0
        #
        # for start, end in intervals:
        #     if end <= max_end:
        #         count += 1
        #     else:
        #         max_end = end
        #
        # return len(intervals) - count

c = Solution()
print(c.removeCoveredIntervals([[1,4],[3,6],[2,8]]))