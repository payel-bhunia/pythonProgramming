# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Head:
    def __init__(self):
        self.head = None
    def reverse(self, head):
        curr = head
        prev = None
        nxt = None
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def insert(self, A):
        if self.head is None:
            self.head = A
        else:
            h = self.head
            while h.next is not None:
                h = h.next
            h.next = A
    def get_head(self):
        return self.head
class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):
        curr = A
        slow = curr
        fast = curr
        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        head2 = slow
        prev.next = None
        h = Head()
        rev_head = h.reverse(head2)
        head1 = A
        while head1 != None:
            if head1.val != rev_head.val:
                return 0
            head1 = head1.next
            rev_head = rev_head.next
        return 1

if __name__ == "__main__":
    s = Solution()
    inputt = [1,2]
    head = Head()
    for i in inputt:
        A = ListNode(i)
        head.insert(A)
    h = head.get_head()
    print(s.lPalin(h))

