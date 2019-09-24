# """
# LeetCode problem 347: Top K Frequent Elements
# We use a max heap gathered from a dictionary, then use heap_extract_max() for k times.
# Time Complexity: O(klogn), assuming Fibonacci Heap is used.
# """
from typing import List
from queue import PriorityQueue


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        res = []
        pq = PriorityQueue()
        for num in nums:  # O(n)
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        for value, key in d.items():  # O(n) amortized
            pq.put((-key, value))
        # O(klogn) amortized: assuming Fibonacci heap, get is O(logn) amortized performed k times
        for idx in range(k):
            res.append(pq.get(True)[1])
        return res


lst = [5, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 2, 2]
sol = Solution()
lst2 = [1, 1, 1, 2, 2, 3]
sol.topKFrequent(lst, 2)
sol.topKFrequent(lst2, 2)
lst3 = [1]
sol.topKFrequent(lst3, 1)
