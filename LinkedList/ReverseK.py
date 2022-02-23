"""Return reference of new head of the reverse linked list
  The input list will have at least one element
  Node is defined as

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
  This is method only submission.
  You only need to complete the method.
"""


def doReverse(h):
    curr = h
    prv = None
    nxt = None
    tail = curr
    while curr != None:
        nxt = curr.next
        curr.next = prv
        prv = curr
        curr = nxt
    return prv, tail


class Solution:
    def reverse(self, head, k):
        curr = head
        count = 0
        h = None
        while curr != None:
            count += 1
            if count == k:
                nxt = curr.next
                curr.next = None
                if h == None:
                    start, tail = doReverse(head)
                    head = start
                else:
                    start, tail = doReverse(h)
                    prv.next = start
                h = nxt
                tail.next = nxt
                prv = tail
                count = 0
                curr = nxt
            else:
                if curr.next == None:
                    start, tail = doReverse(h)
                    prv.next = start
                    break
                else:
                    curr = curr.next
        return head

        # Code here


# {
#  Driver Code Starts
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        # self.tail

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            # arr.append(str(temp.data))
            temp = temp.next
        print()


if __name__ == '__main__':
    t = 1
    while (t > 0):
        llist = LinkedList()
        n = input()
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)
        k = int(input())
        new_head = LinkedList()
        ob = Solution()
        new_head = ob.reverse(llist.head, k)
        llist.head = new_head
        llist.printList()
        t -= 1

# } Driver Code Ends