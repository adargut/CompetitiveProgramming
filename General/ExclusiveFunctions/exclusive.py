# """
# Exclusive Function
# Using a stack, we determine the runtime of each process on a single-threaded CPU.
# Time Complexity: O(n), Space Complexity: O(n)
# """
from typing import List
import numpy as np


class Solution:
    @staticmethod
    def exclusiveTime(n: int, logs: List[str]) -> List[int]:
        res = np.zeros(n, dtype=int)
        stack = []

        for s in logs:
            f_id, log_type, time = s.split(":")
            f_id, time = int(f_id), int(time)
            if not stack or log_type == 'start':
                stack.append([f_id, time])
            else:
                addition = time - stack.pop()[1] + 1
                res[f_id] += addition
                if stack: # get rid of nested calling duration
                    res[stack[-1][0]] -= addition
        return res


sol = Solution()
print(sol.exclusiveTime(2, ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]))
print(sol.exclusiveTime(2, ["0:start:0", "0:start:2", "0:end:5", "1:start:7", "1:end:7", "0:end:8"]))
