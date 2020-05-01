
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

    def sorted_insert(self,data):
        new_node=ListNode(data)
        if self.head is None:
            self.head=new_node

        elif new_node.val <=self.head.val:
            new_node.next=self.head
            self.head=new_node
        else:
            prev = self.head
            curr = self.head.next
            while curr is not None and curr.val <=new_node.val:
                prev=curr
                curr=curr.next

            new_node.next=curr
            prev.next=new_node


    def display(self):
        curr = self.head
        while curr is not None:
            print(curr.get_data())
            curr = curr.next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        curr=l2.head
        while curr is not None:
            l1.sorted_insert(curr.val)
            curr=curr.next
        return l1

def main():

    l1=LinkedList()
    l1.sorted_insert(3)
    l1.sorted_insert(1)
    l1.sorted_insert(5)
    l2=LinkedList()
    l2.sorted_insert(3)
    l2.sorted_insert(1)
    l2.sorted_insert(5)
    a=Solution()
    l3=a.mergeTwoLists(l1,l2)
    l3.display()

main()