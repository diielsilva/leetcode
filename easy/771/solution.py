class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        map = {}

        for stone in stones:
            if stone in map:
                val = map[stone]
                map[stone] = val + 1
            else:
                map[stone] = 1

        for jewel in jewels:
            if jewel in map:
                ans += map[jewel]
                del map[jewel]

        return ans
