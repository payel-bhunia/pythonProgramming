# User function Template for python3


'''class Node:
    # Constructor to create a new Node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None'''


def getHeight(root, hash_map):
    if root == None:
        return 0
    else:
        lH = getHeight(root.left, hash_map)
        rH = getHeight(root.right, hash_map)
        hash_map[root] = max(lH, rH) + 1
        return max(lH, rH) + 1


def checkBalanced(root, hash_map):
    if root == None:
        return 1
    else:
        if root.left != None:
            lH = hash_map[root.left]
        else:
            lH = 0
        if root.right != None:
            rH = hash_map[root.right]
        else:
            rH = 0
        if abs(lH - rH) > 1:
            return 0
        else:
            return checkBalanced(root.left, hash_map) and checkBalanced(root.right, hash_map)


# Function to check whether a binary tree is balanced or not.
class Solution:
    def isBalanced(self, root):
        hash_map = dict()
        getHeight(root, hash_map)
        return checkBalanced(root, hash_map)

        # add code here


# {
#  Driver Code Starts
# Initial Template for Python 3

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
    ip = s

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
        s = ['1', '2', 'N', 'N', '3']
        root = buildTree(s)
        ob = Solution()
        if ob.isBalanced(root):
            print(1)
        else:
            print(0)
# } Driver Code Ends