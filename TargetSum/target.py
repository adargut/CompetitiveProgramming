# """
# Classic Subset Sum Problem
# We use dynamic programming to find number of subsets of a given set summing to target.
# Time Complexity: O(n*t), where t=target and n=cardinality(set)
# """
from typing import List
import numpy as np


class Solution:
    @staticmethod
    def combinationSum(candidates: List[int], target: int) -> int:
        n = len(candidates)
        c = np.zeros((n, target + 1))

        for i in range(n):
            for j in range(target + 1):
                if j - candidates[i] == 0:
                    c[i][j] = 1 + c[i - 1][j]
                    continue
                if j - candidates[i] > 0:
                    c[i][j] = c[i - 1][j] + c[i][j - candidates[i]]
                    continue
                else:
                    c[i][j] = c[i - 1][j]
        return int(c[n - 1][target])


sol = Solution()
t1 = sol.combinationSum([1, 6, 7], 10)
t2 = sol.combinationSum([1, 10, 18], 12)
t3 = sol.combinationSum([2, 3, 5], 8)

# basic UT
assert t1 == 3
assert t2 == 2
assert t3 == 3
