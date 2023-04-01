from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l != r:
            if nums[(l + r) // 2] < target:
                l = (l + r) // 2 + 1
            else:
                r = (l + r) // 2
        if nums[l] == target:
            return l
        return -1


s = Solution()
assert s.search([-1,0,3,5,9,12], 9) == 4
assert s.search([-1,0,3,5,9,12], 13) == -1