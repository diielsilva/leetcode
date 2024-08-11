class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ans = ""

        for i in range(len(word)):

            if word[i] == ch:

                for j in range(i, -1, -1):
                    ans += word[j]

                for k in range(i + 1, len(word), 1):
                    ans += word[k]

                return ans

        if ans == "":
            return word
