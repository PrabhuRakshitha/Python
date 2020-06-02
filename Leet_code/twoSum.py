#  questionds to be asked
#  can i used same elements twice  say i have  2 ,2 in list and target 4
# Waht if we dont have target sum  in the list


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = dict()

        for i in range(len(nums)):
            temp =target -nums[i]
            if target - nums[i] in nums_dict:
                return [nums_dict[temp], i ]
            else:
                nums_dict[nums[i]] = i


if __name__ =="__main__":
    obj = Solution()
    nums =[ 2, 7 , 11 , 15]
    target = 9
    out=obj.twoSum(nums , target)
    print(out)