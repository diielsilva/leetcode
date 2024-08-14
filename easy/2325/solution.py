class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alphabet = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z"
        ]

        ans = ""
        index = 0
        encoded = {}

        key = key.replace(" ", "")

        for i in range(len(key)):
            if key[i] not in encoded:
                encoded[key[i]] = index
                index += 1

        for i in range(len(message)):
            if message[i] == " ":
                ans += " "
            else:
                val = encoded[message[i]]
                let = alphabet[val]
                ans += let

        return ans
