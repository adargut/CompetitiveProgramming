from typing import List


class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        idx = 0

        while idx < len(A) - 1:
            if A[idx] > A[idx + 1]:  # found a local inversion
                self.swap(A, idx)
                idx += 1
            idx += 1

        print(A)
        idx = 0
        # check if after fixing all local inversions, array is sorted
        while idx < len(A) - 1:
            if A[idx] > A[idx + 1]:
                return False
            idx += 1
        return True

    # fix local inversion
    def swap(self, A: List[int], idx):
        tmp = A[idx]
        A[idx] = A[idx + 1]
        A[idx + 1] = tmp

sol = Solution()
print(sol.isIdealPermutation([1, 0, 2]))