import copy
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        out = []
        def combihelper(candidates, nums=[]):
            # print(sum(nums), nums)
            if target == sum(nums) :
                temp = copy.deepcopy(nums)
                temp.sort()
                # if temp not in out:
                out.append(temp)
                return
            elif sum(nums) > target:
                return
            else:
                for num in candidates:
                    nums.append(num)
                    combihelper(candidates, nums)
                    nums.pop()

        combihelper(candidates)
        return out


if __name__ =="__main__":
    obj = Solution()
    candidate =[2,2]
    target =4
    out = obj.combinationSum(candidate,target)
    print(out)