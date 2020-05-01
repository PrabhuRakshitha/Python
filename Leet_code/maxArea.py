class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        output = 0

        def rec_area(height, l, r, output):
            if r >l:
                if height[l]<height[r]:
                    temp=height[l]
                else:
                    temp=height[r]

                temp=temp *(r-l)

                if temp > output:
                    output=temp

                output=rec_area(height,l,r-1,output)
            return output

        for i in range(len(height)):
            output=rec_area(height,i,len(height)-1,output)

        return output

def main():
    a=Solution()
    print(a.maxArea([1,8,6,2,5,4,8,3,7]))

main()