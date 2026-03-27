class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count = sum(1 for i in word if i.isupper())
        if count == len(word):
            return True
        if count == 1 and word[0].isupper():
            return True
        if count == 0:
            return True
        return False

        # return (
        #         word.isupper()
        #         or word.islower()
        #         or (word[0].isupper() and word[1:].islower())
        # )


c = Solution()
print(c.detectCapitalUse("leetcode"))