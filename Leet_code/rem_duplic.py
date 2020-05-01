
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp= [nums[0]]
        for x in nums:
            if temp[-1] !=x:
                temp.append(x)

        return len(temp)


def main():
    a= Solution()
    nums=[1,3,3,3,5,8,8,9]
    print(a.removeDuplicates(nums))


main()


