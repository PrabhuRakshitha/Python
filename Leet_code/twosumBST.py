# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        BSTstack =[]
        curr =root
        nums_set = set()
        while True:
            if curr is not None:
                if k - curr.val in nums_set:
                    return True
                else:
                    nums_set.add(curr.val)
                BSTstack.append(curr)
                curr = curr.left
            elif BSTstack:
                curr = BSTstack.pop()
                curr = curr.right
            else:
                break

        return False



if __name__ =="__main__":
    obj = Solution()
    nums =[ 2, 7 , 11 , 15]
    target = 9
    out=obj.twoSum(nums , target)
    print(out)
