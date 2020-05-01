class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = 1
        count = 0

        if dividend * divisor < 0:
            sign = -1

        divisor = abs(divisor)

        if divisor == 1:
            count=abs(dividend) * sign
        else:
            sum = divisor
            while sum <= abs(dividend):
                sum = sum + divisor
                count = count + 1

        if count *sign > (2**31)-1:
            return  (2**31)-1
        elif count * sign < (-2**31):
            return  (-2**31)
        else:
            return count *sign

