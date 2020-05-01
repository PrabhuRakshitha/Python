class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res =1
        zero_cnt=0
        output = list()
        for x in nums:
            if x ==0:
                zero_cnt=zero_cnt+1
            else:
                res = res *x
        if zero_cnt >1:
            output =[0]*len(nums)
            return output

        if zero_cnt == 1:
            output = [0] * len(nums)
            output[nums.index(0)] = res
            return output
        for x in nums:
            output.append(res//x)

        return output

def main():
    obj = Solution()
    A = [1,0,3,0]
    print(obj.productExceptSelf(A))

main()