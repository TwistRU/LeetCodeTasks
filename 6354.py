class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ost = k
        ans = 0
        if ost > 0:
            ans += min(ost, numOnes)
            ost -= min(ost, numOnes)
        if ost > 0:
            ost -= min(ost, numZeros)
        if ost > 0:
            ans -= ost
        return ans


s = Solution()
assert s.kItemsWithMaximumSum(3, 2, 0, 2) == 2
assert s.kItemsWithMaximumSum(3, 2, 0, 4) == 3
