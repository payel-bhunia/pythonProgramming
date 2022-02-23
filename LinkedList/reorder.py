class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printlist(self, head_name):
        ref = head_name
        while ref.next is not None:
            print(ref.data, '-->', end="")
            ref = ref.next
        if ref is not None:
            print(ref.data)

    def push_data(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            ref = self.head
            while ref.next is not None:
                ref = ref.next
            ref.next = Node(data)

def reverse(head):
    curr = head
    nxt = None
    prev = None
    while curr is not None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    head = prev
    return head


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reorderList(self, A):
        if A is None:
            return A
        elif A.next is None:
            return A
        elif A.next.next is None:
            return A
        else:
            start = A
            end = A
            while end.next.next is not None:
                end = end.next.next
                prev = start
                start = start.next
                if end.next is None:
                    break
            head2 = reverse(start.next)
            start.next = None
            head1 = A
            curr1 = A
            curr2 = head2
            while head2 is not None:
                curr2 = head2
                head2 = head2.next
                nxt = curr1.next
                curr1.next = curr2
                curr2.next = nxt
                curr1 = nxt
            return head1

if __name__ == "__main__":
    llist = LinkedList()
    llist.push_data(30)
    llist.push_data(3)
    llist.push_data(4)
    llist.push_data(20)
    llist.push_data(5)
    llist.push_data(6)
    llist.printlist(llist.head)
    s = Solution()
    head1 = s.reorderList(llist.head)
    ans = LinkedList()
    ans.head = head1
    print('----after----')
    ans.printlist(ans.head)
    #30-->3-->4-->20-->5-->6







