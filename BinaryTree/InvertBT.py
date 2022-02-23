from collections import deque

class TreeNode:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def doInvert(root):
    if root.left != None and root.right!= None:
        rH = doInvert(root.right)
        lH = doInvert(root.left)
        root.left = rH
        root.right = lH
    elif root.left != None:
        root.right = doInvert(root.left)
        root.left = None
    elif root.right!= None:
        root.left = doInvert(root.right)
        root.right = None
    return root





class Solution:
    def invertTree(self, A):
        doInvert(A)
        return A


# {
#  Driver Code Starts
# Initial Template for Python 3

# Function to Build Tree
def buildTree(s):
    # Corner Case
    if (len(s) == 0 or s[0] == "-1"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = s

    # Create the root of the tree
    root = TreeNode(int(ip[0]))
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
            currNode.left = TreeNode(int(currVal))

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
            currNode.right = TreeNode(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root

def postorder_traverse(root,ans):
        if root != None:
            if root.left:
                postorder_traverse(root.left,ans)
            if root.right:
                postorder_traverse(root.right,ans)
            ans.append(root.data)

if __name__ == "__main__":
    s = ['9','2','1','4','-1','-1','3']
    ans = []
    root = buildTree(s)
    root1 = Solution().invertTree(root)
    postorder_traverse(root1,ans)
    for i in ans:
        print(i,'-->',end="")
    print()
# } Driver Code Ends