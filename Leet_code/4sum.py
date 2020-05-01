class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums=sorted(nums)
        mid=len(nums)//2
        subset_2=[]
        i=0
        j=mid
        output=[]

        if len(nums) <4:
            return output
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    for l in range(k+1, len(nums)):
                        temp=[nums[i],nums[j],nums[k],nums[l]]
                        if sum(temp)==target and temp not in output:
                            output.append(temp)

        return output


def main():
    a=Solution()
    print(a.fourSum([1, 0, -1, 0, -2, 2],0))

main()