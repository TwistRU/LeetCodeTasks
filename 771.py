class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        for jew in jewels:
            for stone in stones:
                ans += jew == stone
        return ans