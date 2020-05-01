class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)

        j = 0
        i = 0
        v_len = len(nums)
        while True:
            if i < v_len:
                count = nums.count(nums[i])
            else :
                break

            print('i :',i ,' j :',j)
            print('count:', count,'element:',nums[i])
            if count == 1:
                nums[j] = nums[i]
                j = j+1
            elif count >1:
                nums[j]= nums[i]
                nums[j+1] = nums[i]
                j = j+2
            i = i+count
        return j+1

def main():
    a=Solution()
    x=[1,1,1,2,2,3]
    print(a.removeDuplicates(x))

main()
