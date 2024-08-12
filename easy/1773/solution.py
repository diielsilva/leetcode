class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        ans = 0

        match ruleKey:
            case "type":
                ruleKey = 0
            case "color":
                ruleKey = 1
            case "name":
                ruleKey = 2

        for i in range(len(items)):
            if items[i][ruleKey] == ruleValue:
                ans += 1

        return ans
