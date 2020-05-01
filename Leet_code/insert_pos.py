class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i]>=target:
                return i
        return i+1

def main():
    a=Solution()
    nums =[1,4,6,8,9]
    print(a.searchInsert(nums ,2))


main()

