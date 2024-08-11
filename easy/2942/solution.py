class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        ans = []

        for i in range(len(words)):
            if words[i].__contains__(x):
                ans.append(i)

        return ans
