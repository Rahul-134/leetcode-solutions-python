class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # return str(int(num1) * int(num2))
        def convert_str_to_int(num: str) -> int:
            output: int = 0
            for i, val in enumerate(reversed(num)):
                output += int(val) * (10 ** i)
            return output

        return str(convert_str_to_int(num1) * convert_str_to_int(num2))

c = Solution()
print(c.multiply("2", "3"))