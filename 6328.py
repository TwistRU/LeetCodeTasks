import string
from typing import List


class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        d = dict(zip(string.ascii_lowercase, range(1, len(string.ascii_lowercase) + 1)))
        d.update(zip(chars, vals))
        nums = list(map(lambda x: d[x], s))
        cur_max, max_until_now = 0, 0
        for num in nums:
            cur_max = max(num, num + cur_max)
            max_until_now = max(max_until_now, cur_max)
        return max_until_now

