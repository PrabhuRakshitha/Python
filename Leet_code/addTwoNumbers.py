#  My assumption
#  given linked list is in reverse order  and hence we start to add 2 linked list
# there is no leading zero
# we do not have any sign to the number , unsigned number
#  return would be another linked list




# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        rem =0
        l3 =None
        while l1 and l2:
            temp_node =  ListNode()
            temp_node.val = (l1.val + l2.val +rem) % 10
            rem =  (l1.val + l2.val) //10

            if l3 is None:
                l3 =temp_node
                head =l3
            else:
                l3.next =temp_node
                l3 =l3.next

            l1= l1.next
            l2= l2.next

        while l1:
            if rem:
                l3.next =ListNode()
                l3 =l3.next
                l3.val =(l1.val + rem ) %10
                rem = (l1.val+ rem) //10
                l1=l1.next
            else:
                l3.next =l1

        while l2:
            if rem:
                l3.next = ListNode()
                l3 = l3.next
                l3.val = (l2.val + rem) % 10
                rem = (l2.val + rem) // 10
                l2= l2.next
            else:
                l3.next = l2

        if rem:
            l3.next = ListNode()
            l3 = l3.next
            l3.val=rem

        return head






