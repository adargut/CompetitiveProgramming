from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, 1]
        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, 1]
        left, right = self.searchLeft(nums, target), self.searchRight(nums, target)

        return [left, right]

    def searchLeft(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while start < end:
            mid = int((start + end) / 2)
            print(start, end, mid)
            if nums[mid - 1] != target and nums[mid] == target and nums[mid + 1] != target:
                return mid
            if nums[mid - 1] != target and nums[mid] == target:  # target found
                return mid
            elif nums[mid] == target or nums[mid] > target:  # search left half
                end = mid - 1
            else:
                start = mid + 1  # search right left
        return -1

    def searchRight(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = int((start + end) / 2)
            if (not nums[mid+1] or nums[mid + 1] != target) and nums[mid] == target:  # target found
                return mid
            elif nums[mid] == target or nums[mid] < target:  # search right part
                start = mid + 1
            else:
                end = mid - 1  # search left part
        return 1

sol = Solution()
nums = [5,7,7,8,8,10]
res = sol.searchRange(nums, 10)
print(res)