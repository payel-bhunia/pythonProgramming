# Definition for singly-linked list.
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
    last_node = curr
    while curr is not None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    head = prev
    return head, last_node


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def reverseList(self, A, B):
        if B < 2:
            return A
        ans = LinkedList()
        head = A
        while head is not None:
            count = 1
            start = head
            end = head
            while count < B and end is not None:
                end = end.next
                count += 1
            print(start,end)
            next_node = end.next
            end.next = None
            head1, last = reverse(start)
            if ans.head is None:
                ans.head = head1
            else:
                ans_last.next = head1
            ans_last = last
            last.next = next_node
            head = next_node
        return ans.head

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
    head1 = s.reverseList(llist.head, 3)
    ans = LinkedList()
    ans.head = head1
    llist.printlist(ans.head)





