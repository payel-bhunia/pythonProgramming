# User function Template for python3

''' structure of list node:

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

'''


class Solution:
    def findIntersection(self, head1, head2):
        # code here
        hash_set = set()
        curr = head2
        while curr != None:
            hash_set.add(curr.data)
            curr=curr.next
        curr = head1
        prv = None
        head = None
        while curr != None:
            if curr.data in hash_set:
                if prv == None:
                    ll = linkedList()
                ll.insert(curr.data)
                if prv == None:
            curr = curr.next
        return ll.head

        # return head of intersection list


# {
#  Driver Code Starts
# Initial Template for Python 3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next


def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next


if __name__ == '__main__':
    t = 1
    for _ in range(t):

        n1 = int(input())
        arr1 = [int(x) for x in input().split()]
        ll1 = linkedList()
        for i in arr1:
            ll1.insert(i)

        n2 = int(input())
        arr2 = [int(x) for x in input().split()]
        ll2 = linkedList()
        for i in arr2:
            ll2.insert(i)

        result = Solution().findIntersection(ll1.head, ll2.head)
        printList(result)
        print()

# } Driver Code Ends