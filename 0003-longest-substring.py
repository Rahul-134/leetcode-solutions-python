# 3. Longest substring without repeating characters
import numpy as np
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s = np.array(s)
        index = 0
        count = []
        if len(s) == 1:
            return 1
        while index+1 < len(s):
            i = index
            dummy = s[i]
            while i+1 < len(s):
                if (s[i] != s[i+1:][0]) and (s[i+1:][0] not in dummy):
                    dummy += s[i+1:][0]
                    count.append(len(dummy))
                    print(dummy)
                else:
                    break
                i += 1
            index += 1
        return max(count) if len(count) > 0 else 0
a = Solution()
print(a.lengthOfLongestSubstring("au"))