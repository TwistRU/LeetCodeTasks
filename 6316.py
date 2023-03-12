from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        prefix = [0] * len(nums)
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            prefix[i] = s
        # print(nums)
        # print(prefix)
        return sum(map(lambda x: 1 if x > 0 else 0, prefix))

s = Solution()
assert s.maxScore([2,-1,0,1,-3,3,-3]) == 6