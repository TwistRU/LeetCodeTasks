from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        right_border = nums[0]
        cur_i = 0
        while right_border < len(nums) - 1:
            if cur_i > right_border:
                return False
            right_border = max(cur_i + nums[cur_i], right_border)
            cur_i += 1
        return True

s = Solution()
assert s.canJump([2,3,1,1,4]) == True
assert s.canJump([3,2,1,0,4]) == False
assert s.canJump([0,2,3]) == False
