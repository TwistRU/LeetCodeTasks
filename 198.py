from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = 0
        cur = 0
        for i in range(len(nums)):
            prev, cur = cur, max(nums[i] + prev, cur)
        return cur


s = Solution()
assert s.rob([2, 7, 9, 3, 1]) == 12
assert s.rob([2, 1, 1, 2]) == 4
