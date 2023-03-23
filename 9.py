from math import ceil


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        n = 0
        while x // 10 ** n != 0:
            n += 1
        print("Start", x)
        if n % 2 == 1:
            for i in range(n // 2, 0, -1):
                if (x // 10 ** (n // 2 + i)) % 10 != (x // 10 ** (n // 2 - i)) % 10:
                    return False
        else:
            for i in range(n // 2, -1, -1):
                if (x // 10 ** (n // 2 - 1 + i)) % 10 != (x // 10 ** (n // 2 - i)) % 10:
                    return False
        return True

s = Solution()
assert s.isPalindrome(1234321)
assert s.isPalindrome(123321)
assert not s.isPalindrome(-121)
assert not s.isPalindrome(123)
assert not s.isPalindrome(10)

