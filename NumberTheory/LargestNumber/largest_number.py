# """
# LeetCode problem 179: Largest Number
# We simply replace the default comparator with a 'concatenation' type comparator, then sort according to it.
# Time Complexity: O(nlogn)
# """
from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = sorted(nums, key=cmp_to_key(self.compare))
        # handle edge case of all 0s
        if nums[0] == 0:
            return "0"
        result = ""
        for num in nums:
            result += str(num)
        return result

    # use custom comparator
    def compare(self, num1: int, num2: int):
        num1 = str(num1)
        num2 = str(num2)
        if num1 == num2:
            return 0
        elif num1 + num2 > num2 + num1:
            return -1
        else:
            return 1


sol = Solution()
print(sol.largestNumber([10, 2]))
print(sol.largestNumber([3, 30, 34, 5, 9]))
print(sol.largestNumber([0, 0, 0]))
