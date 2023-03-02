class Solution:
    memo = {-1: 0, 0: 1}

    def climbStairs(self, n: int) -> int:
        if n not in self.memo:
            self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.memo[n]
