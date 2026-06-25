class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        current_count = sum(1 for char in s[:k] if char in vowels)
        max_count = current_count

        for i in range(k, len(s)):
            if s[i] in vowels:
                current_count += 1
            if s[i - k] in vowels:
                current_count -= 1

            if current_count > max_count:
                max_count = current_count

        return max_count

c = Solution()
print(c.maxVowels("abciiidef", 3))