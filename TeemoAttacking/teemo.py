from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if len(timeSeries) == 0: return 0
        pois = 0
        for idx in range(len(timeSeries) - 1):
            pois += min((timeSeries[idx + 1] - timeSeries[idx]), duration)
        pois += duration
        return pois


print(Solution().findPoisonedDuration([1, 4], 2))
