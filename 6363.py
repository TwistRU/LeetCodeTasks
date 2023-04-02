from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans = []
        count = [0] * 201
        for i in nums:
            count[i] += 1
        while sum(count) != 0:
            cur = []
            for i in range(1, 201):
                if count[i] > 0:
                    cur.append(i)
                    count[i] -= 1
            ans.append(cur)
        print(ans)
        return ans





s = Solution()
assert s.findMatrix([1,3,4,1,2,3,1]) == [[1,3,4,2],[1,3],[1]]