class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        counter =1
        out = x
        multiplier = x
        i = 1
        while True:
            if n == 0:
                out = 1
                break
            elif counter == abs(n) :
                break
            elif counter * i <= abs(n):
                out = out * multiplier
                counter = counter + i
                multiplier = multiplier * multiplier
                i = i * 2
            else:
                multiplier = multiplier / x
                i = i-1
        if n < 0:
            return (1/out)
        else:
            return out


if __name__ =="__main__":
    obj = Solution()
    out = obj.myPow(1.0003,231)
    print(out)






