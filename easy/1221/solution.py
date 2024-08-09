class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0
        aux = {}

        for i in range(len(s)):
            if s[i] in aux:
                val = aux[s[i]]
                aux[s[i]] = val + 1
            else:
                aux[s[i]] = 1

            if len(aux.keys()) == 2:
                val1 = aux["L"]
                val2 = aux["R"]

                if val1 == val2:
                    ans += 1
                    aux.clear()

        return ans
