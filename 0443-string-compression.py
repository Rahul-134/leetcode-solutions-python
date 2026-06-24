from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 1
        i, j = 0, 1
        s = ""
        while j < len(chars):
            if chars[i] == chars[j]:
                count += 1
                i += 1
                j += 1
            else:
                s += chars[i]
                if count > 1:
                    s += str(count)
                count = 1
                i = j
                j = i + 1
        else:
            s += chars[i]
            if count > 1:
                s += str(count)
            count = 1
        chars.clear()
        for i in s:
            chars.append(i)
        return len(chars)

c = Solution()
print(c.compress(["a","a","a","b","b","a","a"]))