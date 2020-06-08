class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        if x < 0:
            sign = -1
        temp = 0
        while x > 0:
            temp = temp * 10 + (x % 10)
            x = x // 10

        if temp * sign > (2 ** 31 - 1):
            return (2 ** 31 - 1)
        elif temp * sign < (-2 ** 31):
            return (-2 ** 31)
        else:
            return temp * sign