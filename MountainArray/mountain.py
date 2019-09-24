# """
# LeetCode problem 1059: Find in Mountain Array
# We first find the peak using binary search, then perform two more binary searches on both parts of the array.
# Time Complexity: O(logn)
# """

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()
        start = 0
        end = length
        peak = Solution().findPeak(mountain_arr, start, end)
        res = Solution().binarySearchAsc(mountain_arr, start=start, end=peak, target=target)
        if (res >= 0):
            return res
        res = Solution().binarySearchDesc(mountain_arr, start=peak, end=peak, target=target)
        return res

    # utilize binary search to find peak of mountain
    def findPeak(self, mountain_arr: 'MountainArray', start: int, end: int) -> int:
        mid = int((start + end) / 2)
        # peak found
        if mountain_arr.get(mid - 1) < mountain_arr.get(mid) and mountain_arr.get(mid) > mountain_arr.get(mid + 1):
            return mid
        if mountain_arr.get(mid - 1) < mountain_arr.get(mid):
            # we are in the descending part
            return self.findPeak(mountain_arr, mid + 1, end)
        else:
            # we are in the ascending part
            return self.findPeak(mountain_arr, start, mid)

    def binarySearchAsc(self, mountain_arr: 'MountainArray', start: int, end: int, target: int) -> int:
        while start < end:
            mid = int((start + end) / 2)
            if mountain_arr.get(mid) == target:
                return mid
            if mountain_arr.get(mid) < target:
                start = mid - 1
            else:
                end = mid
        return -1

    def binarySearchDesc(self, mountain_arr: 'MountainArray', start: int, end: int, target: int) -> int:
        while start < end:
            mid = int((start + end) / 2)
            if mountain_arr.get(mid) == target:
                return mid
            if mountain_arr.get(mid) > target:
                start = mid + 1
            else:
                end = mid
        return -1


arr = [1, 3, 7, 8, 10, 12, 15, 100, 96, 92, 10, 4, 2]
sol = Solution()
print(sol.findPeak(arr, 0, len(arr)))
