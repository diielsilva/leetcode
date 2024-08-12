class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        first = ""
        last = ""

        for word in word1:
            first += word

        for word in word2:
            last += word

        return first == last
