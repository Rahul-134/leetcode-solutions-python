from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        coords = [0, 0]
        points = []
        obstacles_set = {tuple(obs) for obs in obstacles}
        dir = {
            "North": [1, "West", "East"],
            "East": [1, "North", "South"],
            "South": [-1, "East", "West"],
            "West": [-1, "South", "North"]
        }
        current = "North"

        for i in commands:
            if i == -1 or i == -2:
                current = dir.get(current)[i]
                continue
            if current == "North" or current == "South":
                for k in range(1, abs(i)+1):
                    coords[1] += dir.get(current)[-3]
                    if tuple(coords) in obstacles_set:
                        coords[1] -= dir.get(current)[-3]
                        break
            if current == "East" or current == "West":
                for k in range(1, abs(i) + 1):
                    coords[0] += dir.get(current)[-3]
                    if tuple(coords) in obstacles_set:
                        coords[0] -= dir.get(current)[-3]
                        break
            points.append(coords[:])
        maxDistance = list(map(lambda x: x[0]**2 + x[1]**2, points))
        return max(maxDistance)

c = Solution()
print(c.robotSim([6,-1,-1,6], [[0,0]]))