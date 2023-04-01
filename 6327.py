from typing import List


class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        not_unique = []
        for i in nums1:
            if i in nums2:
                not_unique.append(i)
        if len(not_unique) != 0:
            return min(not_unique)
        m1 = min(nums1)
        m2 = min(nums2)
        return min(m2, m1) * 10 + max(m2, m1)
