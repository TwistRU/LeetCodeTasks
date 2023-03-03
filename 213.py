from typing import List


class Solution:
    def _rob(self, nums, start, end):
        prev = 0
        cur = 0
        for i in range(start, len(nums) + end):
            prev, cur = cur, max(nums[i] + prev, cur)
        return cur

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        return max(self._rob(nums, 0, -1), self._rob(nums, 1, 0))


s = Solution()
assert s.rob([2,3,2]) == 3
assert s.rob([1,2,3,1]) == 4
assert s.rob([1,2,3]) == 3
assert s.rob([1,2]) == 2
assert s.rob([1]) == 1
