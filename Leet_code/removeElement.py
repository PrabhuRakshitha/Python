class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for i in range(nums.count(val)):
            nums.remove(val)
        return(len(nums))

def main():
    a=Solution()
    print(a.removeElement([3,2,2,3],3))

main()
