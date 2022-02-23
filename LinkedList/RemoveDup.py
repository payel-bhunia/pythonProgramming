# User function Template for python3

"""
# Linked list Node class

    class Node :
        def __init__(self, val):
            self.data = val
            self.next = None

"""


class Solution:
    def removeAllDuplicates(self, head):
        # code here
        start = head
        end = head.next
        flag = 0
        prv = None
        while end != None:
            if start.data == end.data:
                flag = 1
                end = end.next
            else:
                if flag == 1:
                    if start == head:
                        head = end
                    else:
                        prv.next = end
                    start = end
                    end = end.next
                    flag = 0
                else:
                    prv = start
                    start = end
                    end = end.next
            if flag == 1:
                if start == head:
                    head = end
                else:
                    prv.next = end
        return head


# {
#  Driver Code Starts
# Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    # prints the elements of linked list starting with head
    def printList(self, head):
        if head is None:
            print(' ')
            return
        curr_node = head
        while curr_node:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next
        print(' ')


if __name__ == '__main__':
    t = 1
    for cases in range(t):
        N = 5 #int(input())
        a = LinkedList()  # create a new linked list 'a'.
        nodes = [1,1,2,2,3] #list(map(int, input().strip().split()))
        for x in nodes:
            a.append(x)
        ob = Solution()
        head = ob.removeAllDuplicates(a.head)
        a.printList(head)
# } Driver Code Ends