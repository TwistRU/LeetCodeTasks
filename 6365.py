from typing import List

# NOT COMPLETED
class Solution:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        ans = [-1] * n
        ans[p] = 0
        for start in range(p, n - k):
            if ans[start] != -1:
                for step in range(1 + k % 2, k, 1 + k % 2)