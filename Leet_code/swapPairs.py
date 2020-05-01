# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        prev=head
        curr=head.next
        while curr is not None:
            if prev==head:
                temp=head.val
                head.val=curr.val
                curr.val=temp
            else:
                temp=prev.val
                prev.val=curr.val
                curr.val=temp

            prev=curr.next
            if prev is None:
                return head
            else:
                curr=prev.next

        return head