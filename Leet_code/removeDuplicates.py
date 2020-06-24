class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) > 1:
            i = 1
        else:
            return nums

        while i < len(nums):
            if nums[i] == nums[i-1]:
                nums.remove(nums[i])
            else:
                i = i+1
        return nums


if __name__ =="__main__":
    obj = Solution()
    nums =[1,1]
    out =obj.removeDuplicates(nums)
    print(out)


