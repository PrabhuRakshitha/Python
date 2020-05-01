

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
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_curr=l1.head
        l2_curr=l2.head
        l3=LinkedList()
        rem=0
        while l1_curr is not None or l2_curr is not None:
            sum =(l1_curr.val +l2_curr.val) %10 +rem
            rem=(l1_curr.val +l2_curr.val) //10
            l3.insert(sum)
            l1_curr = l1_curr.next
            l2_curr = l2_curr.next

        return l3








def main():

    l1=LinkedList()
    l1.insert(3)
    l1.insert(4)
    l1.insert(2)
    l2=LinkedList()
    l2.insert(4)
    l2.insert(6)
    l2.insert(5)
    a=Solution()
    l3=a.addTwoNumbers(l1,l2)
    l3.display()


main()