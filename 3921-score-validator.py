class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        score, counter = 0, 0
        for i in events:
            if counter == 10:
                break
            if i.isdigit():
                score += int(i)
            elif i == "W":
                counter += 1
            else:
                score += 1
        return [score, counter]

c = Solution()
print(c.scoreValidator(["1","4","W","6","WD"]))