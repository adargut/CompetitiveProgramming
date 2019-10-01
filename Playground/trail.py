from math import floor


class Solution:
    def trailingZeroes(self, n: int) -> int:
        trailing = 0

        while floor(n / 5) > 0:
            trailing += floor(n / 5)
            n /= 5
        return trailing


print(Solution().trailingZeroes(667))
