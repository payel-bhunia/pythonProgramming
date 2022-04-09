# User function Template for python3

#User function Template for python3
def findLCA(root,n1,n2,ans,curr):
    if root == None or len(ans) == 2:
        return
    if root.data == n1 or root.data == n2:
        curr.append(root)
        ans.append(curr)
        if len(ans) == 2:
            return
    else:
        curr.append(root)
    findLCA(root.left,n1,n2,ans,curr.copy())
    findLCA(root.right,n1,n2,ans,curr.copy())
    curr.pop()

def findLCA1(root, n1, n2, ans, curr,llist):
    if root == None or len(ans) == 2:
        return
    if root.data == n1 or root.data == n2:
        curr.append(root)
        llist.append(root.data)
        ans.append(curr.copy())
        if len(ans) == 2:
            return
    else:
        curr.append(root)
    llist.append(root.data)
    findLCA1(root.left, n1, n2, ans, curr.copy(),llist.copy())
    findLCA1(root.right, n1, n2, ans, curr.copy(),llist.copy())
    curr.pop()


class Solution:
    # Function to return the lowest common ancestor in a Binary Tree.
    def lca(self, root, n1, n2):
        ans = []
        curr = []
        count = [0]
        llist = []
        findLCA1(root, n1, n2, ans, curr,llist)
        print(ans[0])
        print(ans[1])
        for i in ans[0]:
            print(i.data,end = ' ')
        print('-----')
        for i in ans[1]:
            print(i.data,end = ' ')
        print('-----')
        if len(ans) == 2:
            i = 0
            while i < len(ans[0]) and i < len(ans[1]):
                if ans[0][i] == ans[1][i]:
                    i += 1
                else:
                    break
            return ans[0][i - 1]
        else:
            return Node(-1)

        # Code here


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


if __name__ == "__main__":
    t = 1
    for _ in range(0, t):
        a = 2
        b= 5
        #a, b = list(map(int, input().split()))
        s = '1 2 3 -1 -1 4 -1 -1 5 -1 -1'
        root = buildTree(s)
        k = Solution().lca(root, a, b)
        print(k.data)

# } Driver Code Ends