from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        a = []
        for i in tokens:
            if is_integer(i):
                a.append(int(i))
            elif i == "+":
                l, f = a.pop(), a.pop()
                a.append(f + l)
            elif i == "-":
                l, f = a.pop(), a.pop()
                a.append(f - l)
            elif i == "*":
                l, f = a.pop(), a.pop()
                a.append(f * l)
            elif i == "/":
                l, f = a.pop(), a.pop()
                a.append(int(f / l))
        return int(a.pop())

def is_integer(text):
    try:
        int(text)
        return True
    except ValueError:
        return False

c = Solution()
print(c.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))