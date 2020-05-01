class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(num) < 1:
            return 0
        curr_sum = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            if curr_sum < 0:
                curr_sum = nums[i]
            else:
                curr_sum = curr_sum + nums[i]
            max_sum = max(curr_sum, max_sum)

        return max_sum