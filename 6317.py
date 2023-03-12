from typing import List
from collections import Counter
from math import comb


class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        prefix = [0] * (len(nums) + 1)
        s = 0
        for i in range(len(nums)):
            s ^= nums[i]
            prefix[i] = s
        c = Counter(prefix)
        count = 0
        for i in filter(lambda x: c[x] >= 2, c):
            count += comb(c[i], 2)
        return count

s = Solution()

assert s.beautifulSubarrays([4,3,1,2,4]) == 2
assert s.beautifulSubarrays([1,10,4]) == 0
assert s.beautifulSubarrays([0]) == 1
assert s.beautifulSubarrays([0, 0]) == 3
