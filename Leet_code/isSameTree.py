# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def inorder(root ,v_list):

            if root:
                v_list.append(root.val)
                v_list=inorder(root.left,v_list)
                v_list=inorder(root.right,v_list)

            return v_list
        node_list1=list()
        node_list2=list()
        node_list1=inorder(p,node_list1)
        node_list2=inorder(p,node_list2)

        return node_list1==node_list2

