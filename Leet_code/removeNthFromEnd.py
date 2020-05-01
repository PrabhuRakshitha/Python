# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

    def get_data(self):
        return self.val

    def set_next(self,next_node):
        self.next=next_node


class LinkedList(object):
    def __init__(self):
        self.head = None

    def insert(self,data):
        new_node = ListNode(data)
        new_node.set_next(self.head)
        self.head = new_node

    def display(self):
        curr = self.head
        while curr is not None:
            print(curr.get_data())
            curr = curr.next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        curr=head
        count=0
        while curr is not None:
            count=count+1
            curr=curr.next

        curr = head
        i=0
        while curr is not None:
            if count==n:
                return curr.next
            i=i+1
            if i==(count-n+1):
                prev.next=curr.next

            prev=curr
            curr=curr.next

def main():
    a=Solution()
    print(a.removeNthFromEnd())


main()
