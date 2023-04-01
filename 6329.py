from typing import List
from math import ceil

#NOT COMPLETED
class Solution:
    @staticmethod
    def makeSubKSumEqual(arr: List[int], k: int) -> int:
        if k == 1:
            arr.sort()
            sred = arr[len(arr) // 2]
            ans = sum(map(lambda x: abs(sred - x), arr))
            return ans
        prices = [0] * len(arr)
        for i in range(len(arr)):
            if i + k < len(arr):
                sred = ceil((arr[i] + arr[i + k]) / 2)
                prices[i] += sred - arr[i]
                prices[i + k] += sred - arr[i + k]
                arr[i], arr[i + k] = sred, sred
            else:
                sred = ceil((arr[i] + arr[len(arr) - i - k]) / 2)
                prices[i] += sred - arr[i]
                prices[len(arr) - i - k] += sred - arr[len(arr) - i - k]
                arr[i], arr[len(arr) - i - k] = sred, sred
        return sum(map(abs, prices))


s = Solution()
assert s.makeSubKSumEqual([1, 4, 1, 3], 2) == 1
assert s.makeSubKSumEqual([2, 5, 5, 7], 3) == 5
assert s.makeSubKSumEqual([2, 10, 9], 1) == 8
assert s.makeSubKSumEqual([10, 3, 8], 2) == 7
