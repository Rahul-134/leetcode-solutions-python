class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        flag = True
        ds = {}
        dt = {}
        for i in s:
            ds.setdefault(i, s.count(i))
        for i in t:
            dt.setdefault(i, t.count(i))
        for i, j in ds.items():
            if j != dt.get(i):
                flag = False
                break
        return flag

        # if len(s) != len(t):
        #     return False
        #
        # for i in set(s):
        #     if s.count(i) != t.count(i):
        #         return False
        #
        # return True

c = Solution()
print(c.isAnagram("anagram", "nagaram"))