from collections import defaultdict
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(bool)
        for i, num in enumerate(nums):
            if d[target - num]:
                return [nums.index(target - num), i]
            d[num] = True


s = Solution()
assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
