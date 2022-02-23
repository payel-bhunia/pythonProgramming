# User function Template for python3

def sortList(head):
    if head is not None and head.next is not None:
        prev = head
        curr = head.next
        while curr != None:
            if curr.data < prev.data:
                nxt = curr.next
                curr.next = head
                head = curr
                prev.next = nxt
                curr = nxt
            else:
                prev = curr
                curr = curr.next
    return head
    # {


#  Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node


def PrintList(head):
    while head:
        print(head.data, end=' ')
        head = head.next


if __name__ == '__main__':
    t = 1
    for cases in range(t):
        ll = LinkedList()  # create a new linked list 'll1'.
        nodes_ll = [1,2,-3,-4,-5,-6,7,-8,9,10]
        n = len(nodes_ll)
        for nodes in nodes_ll:
            ll.append(nodes)  # add to the end of the list

        head2 = sortList(ll.head)

        PrintList(head2)
        print()

# } Driver Code Ends