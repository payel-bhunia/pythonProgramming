# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self):
        self.head = None

    def insert(self, A):
        if self.head is None:
            self.head = A
        else:
            h = self.head
            while h.next is not None:
                h = h.next
            h.next = A

    def traverse(self):
        h = self.head
        while h is not None:
            if h.next is not None:
                print(h.val, "-->", end="")
            else:
                print(h.val)
            h = h.next

    def reverse_list(self):
        curr = self.head
        prev = None
        nextt = None
        while curr is not None:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt

        self.head = prev

    def binary_sort(self):
        curr = self.head
        prev = None
        while curr.next != None:
            prev = curr
            curr = curr.next
            if prev.val > curr.val:
                prev.next = curr.next
                curr.next = self.head
                self.head = curr


    def rotateRight(self, B):
        head = self.head
        leng = 0
        while head != None:
            leng += 1
            if head.next is None:
                last_node = head
            head = head.next
        print("last Node is", last_node.val)
        if B < leng:
            count = 0
            head = self.head
            while count != B - leng:
                count += 1
                if count != leng - B:
                    head = head.next
                else:
                    break
            print("last node will be", head.val)
            last_node.next = self.head
            self.head = head.next
            head.next = None


    def reorderList(self):
        length = 0
        curr = self.head
        while curr:
            length += 1
            curr = curr.next
        pos = (length // 2) + 2
        curr = self.head
        head2 = None
        i = 1
        while i < pos:
            i += 1
            if i == pos:
                prev = curr
            curr = curr.next
        prev.next = None
        head2 = curr
        prev = None
        nxt = None
        while curr != None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        head2 = prev
        curr = head2
        head1 = self.head
        while curr:
            nxt = head1.next
            head1.next = ListNode(curr.val)
            head1.next.next = nxt
            curr = curr.next
            head1 = head1.next.next

    def reverse_kth(self,B):
        curr = self.head
        prev = None
        nxt = None
        count = 1
        while count <= B:
            nxt = curr.next
            if prev == None:
                last_ele = curr
            curr.next = prev
            count += 1
            if count > B:
                self.head = curr
                last_ele.next = nxt
                break
            prev = curr
            curr = nxt
        for i in range(B):
            pass

    def reverseBetween(self, B, C):
        A = self.head
        if B == C:
            return A
        count = 1
        curr = A
        start = A
        last_ele = None
        next_ele = None
        while curr:
            if count == B - 1:
                last_ele = curr
                start = curr.next
            if count == C:
                next_ele = curr.next
                curr.next = None
                if last_ele is not None:
                    last_ele.next = next_ele
                else:
                    A = next_ele
            curr = curr.next
            count += 1
        prev = None
        nxt = None
        curr = start
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        start = prev
        if last_ele:
            last_ele.next = start
        else:
            self.head = start
        if next_ele:
            while start.next:
                start = start.next
            start.next = next_ele
        return A


if __name__ == "__main__":
    s = Solution()
    inputt = [3, 6, 9, 6, 3]
    for i in inputt:
        A = ListNode(i)
        s.insert(A)
    #s.traverse()
    s.rotateRight(20)
    s.traverse()
    s.reverse_list()
    s.traverse()
    inputt2 = [1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0]
    bs = Solution()
    for i in inputt2:
        B = ListNode(i)
        bs.insert(B)
    bs.traverse()
    bs.binary_sort()
    bs.traverse()
    inputt3 = [1,2,3]
    reorder = Solution()
    for i in inputt3:
        B = ListNode(i)
        reorder.insert(B)
    reorder.traverse()
    #reorder.reorderList()
    #reorder.traverse()
    reorder.reverseBetween(1,2)
    reorder.traverse()



