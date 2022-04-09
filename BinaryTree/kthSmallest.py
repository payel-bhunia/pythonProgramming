
from collections import deque


class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Node1:
    def __init__(self, summ):
        self.summ = summ


def buildTree(s):
    # Corner Case
    if (len(s) == 0 or s[0] == "-1"):
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
        if (currVal != "-1"):
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
        if (currVal != "-1"):
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root

def inorder(A, ans, i, B):
    if A.left:
        inorder(A.left, ans, i, B)
    else:
        i[0] += 1
        if i[0] == B:
            ans[0] = A.val
            return True
    if A.right:
        inorder(A.right, ans, i, B)

def gen_count(A):
    if A.left is None and A.right is None:
        return Node1(1)
    else:

        


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        ans = [0]
        gen_count(A)
        i = [0]
        inorder(A, ans, i, B)
        return ans[0]

s = Solution()
A = '10 6 15 4 7 13 20'
B = 2
root = buildTree(A)
ans = s.kthsmallest(root,B)
print(ans)