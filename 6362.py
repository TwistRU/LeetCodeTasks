class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        m = 0
        cur_zero = 0
        cur_one = 0
        for i in s:
            if i == "0" and cur_one != 0:
                m = max(min(cur_zero, cur_one) * 2, m)
                cur_one = 0
                cur_zero = 1
            elif i == "0":
                cur_zero += 1
            elif i == "1":
                cur_one += 1
        return max(m, min(cur_zero, cur_one) * 2)



s = Solution()
assert s.findTheLongestBalancedSubstring("01000111") == 6
assert s.findTheLongestBalancedSubstring("111") == 0