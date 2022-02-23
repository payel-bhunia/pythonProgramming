# Your task is to complete this function

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


class Solution:

    # Function to rotate a linked list.
    def rotate(self, head, k):
        # code here
        curr = head
        k -= 1
        while curr.next != None and k > 0:
            curr = curr.next
            k -= 1
        if k == 1:
            start = head
            nxt = curr.next
            curr.next = None
            curr = nxt
            while curr.next != None:
                curr = curr.next
            curr.next = start
            head = nxt
        return head


# {
#  Driver Code Starts
# driver

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next


def printList(n):
    while n:
        print(n.data, end=' ')
        n = n.next
    print()


if __name__ == "__main__":
    for _ in range(1):
        n = int(input())
        arr = [int(x) for x in input().split()]
        k = int(input())

        lis = LinkedList()
        for i in arr:
            lis.insert(i)

        head = Solution().rotate(lis.head, k)
        printList(head)
# } Driver Code Ends