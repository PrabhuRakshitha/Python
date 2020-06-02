class Solution:
    def mySqrt(self, x: int) -> int:
        if x<=1:
            return x
        start,end=0,int(x/2)
        while(start<=end):
            mid=(start+end)//2
            if mid*mid<=x:
                start=mid+1
            else:
                end=mid-1
        return end


if __name__ =="__main__":
    obj = Solution()
    print(obj.mySqrt(4))