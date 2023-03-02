from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        tmp = 0
        for i, x in enumerate(nums):
            tmp += x
            ans[i] = tmp
        print(ans)
        return ans
