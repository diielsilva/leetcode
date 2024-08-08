class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        ans = 0
        aux = {}

        for i in range(len(t)):
            aux[t[i]] = i

        for i in range(len(s)):
            ans += abs(i - aux[s[i]])

        return ans
