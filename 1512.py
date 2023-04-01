from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        origins = [0] * 101
        ans = 0
        for i in nums:
            ans += origins[i]
            origins[i] +=1
        return ans


