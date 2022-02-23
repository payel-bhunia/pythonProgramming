# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def __init__(self):
        self.head = None

    def reverse(self,A):
        curr = A
        prev = None
        nxt = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        A = prev
        return A

    def insert(self, A):
        if self.head is None:
            self.head = A
        else:
            h = self.head
            while h.next is not None:
                h = h.next
            h.next = A

    def lpalin(self):
        length = 0
        head = self.head
        while head:
            length += 1
            head = head.next
        if length == 1:
            return 1
        if length & 1 == 1:
            mid = length // 2 + 1
            odd = 1
        else:
            mid = length // 2
            odd = 0
        head = self.head
        prev = None
        count = 0
        head2 = None
        while head:
            count += 1
            if count == mid:
                if odd == 1:
                    head2 = head.next
                    prev.next = None
                else:
                    head2 = head.next
                    head.next = None
                break
            prev = head
            head = head.next
        head = self.head
        head2 = self.reverse(head2)
        while head and head2:
            if head.val == head2.val:
                head = head.next
                head2 = head2.next
            else:
                break
        if head is None and head2 is None:
            return 1
        else:
            return 0

    def traverse(self):
        h = self.head
        while h is not None:
            if h.next is not None:
                print(h.val, "-->", end="")
            else:
                print(h.val)
            h = h.next

    def mergeTwoLists(self, A, B):
        curr_A = A
        curr_B = B
        head = None
        curr = head
        while curr_A and curr_B:
            if curr_A.val < curr_B.val:
                value = curr_A.val
                curr_A = curr_A.next
            else:
                value = curr_B.val
                curr_B = curr_B.next
            if curr:
                curr.next = ListNode(value)
                curr = curr.next
            else:
                curr = ListNode(value)
        while curr_A:
            if curr:
                curr.next = ListNode(curr_A.val)
                curr = curr.next
            else:
                curr = ListNode(curr_A.val)
            curr_A = curr_A.next
        while curr_B:
            if curr:
                curr.next = ListNode(curr_B.val)
                curr = curr.next
            else:
                curr = ListNode(curr_B.val)
            curr_B = curr_B.next
        return head

    def swapPairs(self):
        A = self.head
        curr = A
        prev = None
        nxt = None
        while curr:
            nxt = curr.next
            if nxt:
                if prev is None:
                    curr.next = nxt.next
                    nxt.next = curr
                    self.head = nxt
                else:
                    curr.next = nxt.next
                    nxt.next = curr
                    prev.next = nxt
                prev = nxt.next
                curr = nxt.next.next
                self.traverse()
            else:
                break

    def reverseList(self, B):
        A = self.head
        curr = A
        count = 0
        head1 = None
        prev = None
        while curr:
            if count == 0:
                head1 = curr
                last_element = curr
            count += 1
            if count == B:
                nxt = curr.next
                curr.next = None
                head1 = self.reverse(head1)
                last_element.next = nxt
                if prev:
                    prev.next = head1
                else:
                    self.head = head1
                prev = last_element
                count = 0
                curr = nxt
                continue
            curr = curr.next


if __name__ == "__main__":
    s = Solution()
    inputt = [6, 10, 0, 3, 4, 8]
    for i in inputt:
        A = ListNode(i)
        s.insert(A)
    s.traverse()
    #p = s.lpalin()
    #s.traverse()
    #s.swapPairs()
    #s.traverse()
    B = 3
    s.reverseList(B)
    s.traverse()




