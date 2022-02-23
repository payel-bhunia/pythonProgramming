# User function Template for python3


'''

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None

'''


def merge(head1, head2):
    curr1 = head1
    prv1 = None
    curr2 = head2
    # prv2 = None
    while curr1 != None and curr2 != None:
        if curr1.data < curr2.data:
            prv1 = curr1
            curr1 = curr1.bottom
        else:
            new = Node(curr2.data)
            if prv1 == None:
                head1 = new
                new.bottom = curr1
            else:
                new.bottom = prv1.bottom
                prv1.bottom = new
            prv1 = new

            curr2 = curr2.bottom
    while curr2 != None:
        prv1.bottom = curr2
        curr2 = curr2.bottom
    return head1

def flatten(root):
    head1 = root
    curr = head1.next
    while curr != None:
        head2 = curr
        nxt = curr.next
        curr.next = None
        head1 = merge(head1, head2)
        head1.next = nxt
        curr = nxt
    return head1

    # Your code here


# {
#  Driver Code Starts
# Initial Template for Python 3

class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
        self.bottom = None


def printList(node):
    while (node is not None):
        print(node.data, end=" ")
        node = node.bottom

    print()


if __name__ == "__main__":
    t = int(input())
    while (t > 0):
        head = None
        N = int(input())
        arr = []

        arr = [int(x) for x in input().strip().split()]
        temp = None
        tempB = None
        pre = None
        preB = None

        flag = 1
        flag1 = 1
        listo = [int(x) for x in input().strip().split()]
        it = 0
        for i in range(N):
            m = arr[i]
            m -= 1
            a1 = listo[it]
            it += 1
            temp = Node(a1)
            if flag == 1:
                head = temp
                pre = temp
                flag = 0
                flag1 = 1
            else:
                pre.next = temp
                pre = temp
                flag1 = 1

            for j in range(m):
                a = listo[it]
                it += 1
                tempB = Node(a)
                if flag1 == 1:
                    temp.bottom = tempB
                    preB = tempB
                    flag1 = 0
                else:
                    preB.bottom = tempB
                    preB = tempB
        root = flatten(head)
        printList(root)

        t -= 1

# } Driver Code Ends