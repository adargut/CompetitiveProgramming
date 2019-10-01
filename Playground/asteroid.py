from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if not asteroids:
            return []
        stack = []
        res = []
        idx = 0

        while idx < len(asteroids):
            if asteroids[idx] > 0:  # asteroid going left
                stack.append(asteroids[idx])  # push asteroid to stack
            else:  # asteroid going right
                last = 0
                destroy = True
                while stack and abs(asteroids[idx]) >= abs(stack[-1]):
                    last = stack.pop()
                    if abs(last) == abs(asteroids[idx]):
                        destroy = False
                        break
                if not stack and destroy:
                    res.append(asteroids[idx])
            idx += 1
        return res + stack


sol = Solution()
print(sol.asteroidCollision([5, 10, -5, -12]))
