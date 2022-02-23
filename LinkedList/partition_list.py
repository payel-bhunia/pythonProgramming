# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class RandomListNode:
     def __init__(self, x):
         self.label = x
         self.next = None
         self.random = None

class Head:
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

    def get_head(self):
        return self.head




class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def traverse(self, A):
        curr = A
        while curr != None:
            if curr.next == None:
                print(curr.val, end="")
            else:
                print(curr.val, '-->', end="")
            curr = curr.next
        print(" ")

    def partition(self, A, B):
        curr = A
        prev = None
        head2 = None
        curr2 = None
        while curr is not None:
            if curr.val >= B:
                if head2 is None:
                    curr2 = curr
                    head2 = curr
                else:
                    curr2.next = curr
                    curr2 = curr2.next
                if prev is None:
                    A = curr.next
                else:
                    prev.next = curr.next
                curr = curr.next
                curr2.next = None
            else:
                prev = curr
                curr = curr.next
        print('head2')
        self.traverse(head2)
        print('head1')
        self.traverse(A)
        if head2 is not None:
            if prev is not None:
                prev.next = head2
            else:
                A = head2
        return A

    def copyRandomList(self, head):
        curr = head
        prev = None
        copied_head = None
        hash_map = {}
        while curr is not None:
            node = ListNode(curr.val)
            if copied_head is None:
                prev = node
                copied_head = prev
            else:
                prev.next = node
                prev = node
            curr = curr.next
        curr = copied_head
        print('copied list')
        while curr != None:
            if curr.next == None:
                print(curr.val, end="")
            else:
                print(curr.val, '-->', end="")
            curr = curr.next
        print(" ")
        #return copied_head


if __name__ == "__main__":
    s = Solution()
    inputt = [ 1,2,3,4,5,6,7]
    B = 4
    head = Head()
    for i in inputt:
        A = ListNode(i)
        head.insert(A)
    h = head.get_head()
    s.traverse(h)
    s.copyRandomList(h)
    hh = s.partition(h,B)
    s.traverse(hh)
    #s.copyRandomList(A)


    #39 -- 36--130--34--12--20--190





