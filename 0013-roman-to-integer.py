class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # total = 0
        # prev_value = 0

        # for char in s:
        #     value = roman_numerals[char]
        #     if prev_value < value:
        #         total += value - 2 * prev_value
        #     else:
        #         total += value
        #     prev_value = value

        # return total
    
        # For lesser time complexity, we can use a single pass approach:
        total = 0
        for i in range(len(s)):
            value = roman_numerals[s[i]]
            if i + 1 < len(s) and roman_numerals[s[i + 1]] > value:
                total -= value
            else:
                total += value
        return total

c = Solution()
print(c.romanToInt("LVIII"))