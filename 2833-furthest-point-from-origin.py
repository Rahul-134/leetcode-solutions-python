class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        # distance = 0
        # for i in moves:
        #     if i == "L":
        #         distance -= 1
        #     elif i == "R":
        #         distance += 1
        # return abs(distance) + moves.count("_")
        return abs(moves.count("L") * (-1) + moves.count("R")) + moves.count("_")

c = Solution()
print(c.furthestDistanceFromOrigin("R_"))