from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:

        # My approach: (uses O(n^2) time complexity)

        count = 0
        val = 1
        d = {}
        values = {}
        for i in word:
            d.setdefault(i, word.count(i))
        d = dict(sorted(d.items(), key = lambda item: item[1], reverse = True))
        for i, j in d.items():
            if count == 8:
                val += 1
                count = 0
            values.setdefault(i, val*j)
            count += 1
        return sum(values.values())

        # O(n) time complexity; uses Counter from collections:

        # frequencies = Counter(word).values()
        # sorted_freqs = sorted(frequencies, reverse=True)
        # total_pushes = 0
        # for index, freq in enumerate(sorted_freqs):
        #     pushes_needed = (index // 8) + 1
        #     total_pushes += freq * pushes_needed
        # return total_pushes

c = Solution()
print(c.minimumPushes("aabbccddeeffgghhiiiiii"))