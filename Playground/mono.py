from typing import List
import numpy as np


class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        N = list(str(N))
        idx, cliffs = 0, True

        while cliffs:
            idx = 0
            while idx < len(N) - 1:
                if N[idx] > N[idx + 1]:  # cliff found
                    N[idx] = str(int(N[idx]) - 1)
                    self.repairCliff(N, idx + 1)
                    cliffs = True
                    break
                else:
                    cliffs = False
                idx += 1

        while idx < len(N) - 1 and cliffs:
            if N[idx] > N[idx + 1]:  # cliff found
                N[idx] = str(int(N[idx]) - 1)
                self.repairCliff(N, idx + 1)
            idx += 1
        return self.toNumber(N)

    def repairCliff(self, N: List[str], at):
        for idx in range(at, len(N)):
            N[idx] = "9"

    def toNumber(self, N: List[str]) -> int:
        idx, power, res = len(N) - 1, 0, 0

        while idx >= 0:
            res += pow(10, power) * int(N[idx])
            idx -= 1
            power += 1
        return res


sol = Solution()
print(sol.monotoneIncreasingDigits(333222))
# sol.checkNumber([1, 5, 3], 143)
