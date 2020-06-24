import copy
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        out = []
        def permuteutil(nums, l, r):
            if l == r:
                temp = copy.deepcopy(nums)
                out.append(temp)

            else:
                for i in range(l,r+1):
                    nums[l], nums[i]= nums[i], nums[l]
                    permuteutil(nums, l+1, r)
                    nums[l] , nums[i] = nums[i], nums[l]

        permuteutil(nums, 0, len(nums) - 1)
        return out

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        out = set()

        def permuteutil(nums, l, r):
            if l == r:
                temp = copy.deepcopy(nums)
                out.add(temp)

            else:
                for i in range(l, r + 1):
                    nums[l], nums[i] = nums[i], nums[l]
                    permuteutil(nums, l + 1, r)
                    nums[l], nums[i] = nums[i], nums[l]

        permuteutil(nums, 0, len(nums) - 1)
        return list(out)


if __name__ =="__main__":
    obj =Solution()
    nums =[1,3,4]
    out=obj.permute(nums)
    print(out)