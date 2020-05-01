class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low=0
        high=x
        while ( low <= high):
            mid=(low+high)/2
            if round(mid * mid)==x:
                return int(mid)
            elif round(mid *mid) > x:
                high=mid
            else:
                low=mid

def main():
    a=Solution()
    print(a.mySqrt(9))

main()