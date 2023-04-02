from typing import List


class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        cost = [(reward1[i] - reward2[i], i) for i in range(len(reward1))]
        cost = sorted(cost, reverse=True)
        ans = 0
        for i in range(k):
            ans += reward1[cost[i][1]]
        for i in range(1, len(reward1) - k + 1):
            ans += reward2[cost[-i][1]]
        return ans


s = Solution()
assert s.miceAndCheese([1,1,3,4], [4,4,1,1], 2) == 15
assert s.miceAndCheese([1,4,4,6,4], [6,5,3,6,1], 1) == 24


