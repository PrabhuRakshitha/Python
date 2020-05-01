class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)/2
        count =dict()
        for i in nums:
            if i in count:
                count[i] += 1
                if count[i] > n:
                    return i
            else:
                count[i] = 1


if __name__ == '__main__':
    obj = Solution()
    arr = [3,3 ,1, 1 ,3,2,2,3,2, 3, 3]

    out = obj.majorityElement(arr)
    print(out)