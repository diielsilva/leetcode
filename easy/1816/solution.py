class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        ans = ""
        s = s.split(" ")

        for i in range(k):
            if i == k - 1:
                ans += s[i]
            else:
                ans += f"{s[i]} "

        return ans
