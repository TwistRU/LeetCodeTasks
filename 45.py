from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = 0
        border = 0
        cur_i = 0
        max_possible_border = border
        while border < len(nums) - 1:
            if cur_i > border:
                steps += 1
                border = max_possible_border
            max_possible_border = max(cur_i + nums[cur_i], max_possible_border)
            cur_i += 1
        return steps


s = Solution()
assert s.jump([2,3,1,1,4]) == 2
assert s.jump([2,3,0,1,4]) == 2
assert s.jump([1]) == 0
