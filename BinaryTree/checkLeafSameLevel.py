# User function Template for python3
def getHeight(root):
    if root == None:
        return 0
    lH = getHeight(root.left)
    rH = getHeight(root.right)
    return max(lH, rH) + 1


def checkLeafSamelevel1(root):
    if root.left != None and root.right != None:
        lH = getHeight(root.left)
        rH = getHeight(root.right)
        if lH == rH:
            return checkLeafSamelevel(root.left) and checkLeafSamelevel(root.right)
        else:
            return False
    elif root.left == None and root.right == None:
        return True
    elif root.left == None:
        return checkLeafSamelevel(root.right)
    elif root.right == None:
        return checkLeafSamelevel(root.left)


def checkLeafSamelevel(root, ht, ht_found_first):
    if root.right == None and root.left == None:
        if ht_found_first[0] == -1:
            ht_found_first[0] = ht
            return True
        else:
            if ht != ht_found_first[0]:
                return False
            else:
                return True
    elif root.right == None:
        return checkLeafSamelevel(root.left, ht + 1, ht_found_first)
    elif root.left == None:
        return checkLeafSamelevel(root.right, ht + 1, ht_found_first)
    else:
        return checkLeafSamelevel(root.left, ht + 1, ht_found_first) and checkLeafSamelevel(root.right, ht + 1,
                                                                                            ht_found_first)


class Solution:
    # Your task is to complete this function
    # function should return True/False or 1/0
    def check(self, root):
        ht = 0
        ht_found_first = [-1]
        ans = checkLeafSamelevel(root, ht, ht_found_first)
        return ans
        # Code here


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
        if Solution().check(root):
            print(1)
        else:
            print(0)

# } Driver Code Ends