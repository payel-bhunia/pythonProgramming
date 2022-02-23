# User function Template for python3

'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''

def reverse(h1):
    prv = None
    curr = h1
    while curr != None:
        nxt = curr.next
        curr.next = prv
        prv = curr
        curr = nxt
    return prv

def mergeResult(h1, h2):
    # return head of merged list
    curr1 = h1
    curr2 = h2
    prev = h1
    while curr1 != None and curr2 != None:
        if curr1.data < curr2.data:
            prev = curr1
            curr1 = curr1.next
        else:
            nxt2 = curr2.next
            if curr1 == h1:
                h1 = curr2
                prev = curr2
            else:
                prev.next = curr2
                prev = curr2
            curr2.next = curr1
            curr2 = nxt2
    if curr2 != None:
        prev.next = curr2
    return reverse(h1)


# {
#  Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Llist:
    def __init__(self):
        self.head = None

    def insert(self, data, tail):
        node = Node(data)

        if not self.head:
            self.head = node
            return node

        tail.next = node
        return node


def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next


if __name__ == '__main__':
    t = 1

    for tcs in range(t):

        n1, n2 = [int(x) for x in input().split()]

        arr1 = [int(x) for x in input().split()]
        ll1 = Llist()
        tail = None
        for nodeData in arr1:
            tail = ll1.insert(nodeData, tail)

        arr2 = [int(x) for x in input().split()]
        ll2 = Llist()
        tail = None
        for nodeData in arr2:
            tail = ll2.insert(nodeData, tail)

        resHead = mergeResult(ll1.head, ll2.head)
        printList(resHead)
        print()

# } Driver Code Ends