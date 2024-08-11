class Solution:
    def interpret(self, command: str) -> str:
        ans = ""
        aux = ""

        for i in range(len(command)):
            if command[i] == "(":

                for j in range(i, len(command), 1):
                    if command[j] == ")":
                        aux += ")"
                        break
                    else:
                        aux += command[j]

                if aux == "()":
                    ans += "o"
                else:
                    ans += "al"

                aux = ""

            elif command[i] == "G":
                ans += "G"

        return ans
