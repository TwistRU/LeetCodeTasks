from typing import List
from itertools import accumulate


class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        left_sum = [0] + list(accumulate(nums))
        right_sum = list(accumulate(nums[::-1]))[::-1][1:] + [0]
        ans = [0] * len(nums)
        for i in range(len(nums)):
            ans[i] = abs(left_sum[i] - right_sum[i])
        return ans

s = Solution()
assert s.leftRigthDifference([10,4,8,3]) == [15,1,11,22]
