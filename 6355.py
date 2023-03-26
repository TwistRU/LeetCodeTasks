from math import floor
from typing import List


class Solution:
    primes = [0] * 1500

    def makePrimes(self):
        prime = [True] * 1500
        prime[0] = False
        for i in range(2, 1500):
            if prime[i]:
                for j in range(2, floor(1500 / i)):
                    prime[i * j] = False
        m = 1500
        for i in range(1499, -1, -1):
            self.primes[i] = m
            if prime[i]:
                m = i
        self.primes[0] = 2

    def primeSubOperation(self, nums: List[int]) -> bool:
        self.makePrimes()
        for i in range(len(nums) - 2, -1, -1):
            if nums[i + 1] <= nums[i]:
                if self.primes[nums[i] - nums[i + 1]] >= nums[i]:
                    return False
                nums[i] -= self.primes[nums[i] - nums[i + 1]]

        return True

s = Solution()
assert s.primeSubOperation([4,9,6,10])
assert not s.primeSubOperation([2, 2])
assert not s.primeSubOperation([623, 4])
assert not s.primeSubOperation([5, 8, 3])
