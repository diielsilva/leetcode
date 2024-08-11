class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        ans = 0

        for sentence in sentences:
            spl = sentence.split(" ")

            if len(spl) > ans:
                ans = len(spl)
            
        return ans