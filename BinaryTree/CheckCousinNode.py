# User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''


def checkForcousin(root, a, b, prev, ht, hash_map, count):
    if root.data == a or root.data == b:
        hash_map[root.data] = (prev, ht)
        count[0] += 1
    if count[0] == 2:
        if hash_map[a][0] != hash_map[b][0] and hash_map[a][1] == hash_map[b][1]:
            return True
        else:
            return False
    if root.left != None  and root.right != None:
        return checkForcousin(root.left, a, b, root, ht + 1, hash_map, count) or checkForcousin(root.right, a, b, root, ht + 1, hash_map, count)
    elif root.right != None:
        return checkForcousin(root.right, a, b, root, ht + 1, hash_map, count)
    elif root.left != None:
        return checkForcousin(root.left, a, b, root, ht + 1, hash_map, count)
    else:
        return

# Returns true if the nodes with values 'a' and 'b' are cousins. Else returns false
def isCousin(root, a, b):
    # Your code here
    prev = None
    ht = 0
    hash_map = dict()
    count = [0]
    return checkForcousin(root, a, b, prev, ht, hash_map, count)


# {
#  Driver Code Starts
# Initial Template for Python 3

# Contributed by Sudarshan Sharma
from collections import deque


# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    # Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


if __name__ == "__main__":
    t = 1
    for _ in range(0, t):
        s = input()
        root = buildTree(s)
        n1, n2 = list(map(int, input().split()))
        ans = isCousin(root, n1, n2)
        if ans:
            print(1)
        else:
            print(0)

# } Driver Code Ends