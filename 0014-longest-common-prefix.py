from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        prefix = ""
        word = strs[0]
        if len(word) == 0:
            return ""
        i = 0
        count = 0
        while i<len(word):
            for k in strs[1:]:
                if k[i:].startswith(word[i]):
                    count += 1
            if count == len(strs[1:]):
                prefix += word[i]
            else:
                break
            i += 1
            count = 0
        return prefix
    
    # 0 ms time complexity
    # if not strs:
    #         return ""
    #     prefix = strs[0]
    #     for s in strs[1:]:
    #         while not s.startswith(prefix):
    #             prefix = prefix[:-1]
    #             if not prefix:
    #                 return ""
    #     return prefix

c = Solution()
print(c.longestCommonPrefix(["cir","car"]))