class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        ans = 0

        for i in range(len(operations)):
            match operations[i][1]:
                case "+":
                    ans += 1
                case "-":
                    ans -= 1

        return ans
