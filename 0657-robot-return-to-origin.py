class Solution:
    def judgeCircle(self, moves: str) -> bool:

        # x = moves.count("L")*-1 + moves.count("R")
        # y = moves.count("D")*-1 + moves.count("U")
        # if x == y == 0:
        #     return True
        # return False

        return moves.count("L") == moves.count("R") and moves.count("D") == moves.count("U")

c = Solution()
print(c.judgeCircle("UD"))