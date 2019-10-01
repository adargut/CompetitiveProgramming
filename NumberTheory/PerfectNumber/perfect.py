import math


class Solution(object):
    def checkPerfectNumber(self, num):
        if num == 1:
            return False
        """
        :type num: int
        :rtype: bool
        """
        sum = 1

        for x in range(2, int(math.sqrt(abs(num)) + 1)):
            if num % x == 0:
                sum += (x + num / x)
        return sum == num