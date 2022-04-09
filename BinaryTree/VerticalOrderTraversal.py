
class Tree:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# User function Template for python3

from collections import deque



# Function to Build Tree
def buildTree(s):
    # Corner Case
    if (len(s) == 0 or s[0] == "-1"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Tree(int(ip[0]))
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
            currNode.left = Tree(int(currVal))

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
            currNode.right = Tree(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


# } Driver Code Ends

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None
def vertical_order(root, ans, ht, key, offset):
    if root is not None:
        if ans[key - offset][ht] == -1:
            ans[key - offset][ht] = [root.val]
        else:
            ans[key - offset][ht].append(root.val)
        vertical_order(root.left, ans, ht + 1, key - 1, offset)
        vertical_order(root.right, ans, ht + 1, key + 1, offset)
    else:
        return

def check_height_width(root, ht, key, key_height):
    if root is not None:
        key_height[0] = min(key_height[0], key)
        key_height[1] = max(key_height[1], key)
        key_height[2] = max(key_height[2], ht)
        check_height_width(root.left, ht + 1, key - 1, key_height)
        check_height_width(root.right, ht + 1, key + 1, key_height)
    else:
        return

class Solution:
    def verticalOrderTraversal(self, A):
        key = 0
        ht = 0
        key_height = [1000000007,-1000000007 ,-1000000007]
        check_height_width(A, ht, key, key_height)
        max_height = key_height[2]
        size = key_height[1]-key_height[0]+1
        ans = []
        for i in range(size):
            temp = [-1] * (max_height+1)
            ans.append(temp)
            temp = []
        offset = key_height[0]
        #print(ans, key, ht, offset,key_height)
        vertical_order(A, ans, ht, key, offset)
        print(ans)
        result = []
        for i in ans:
            tem = []
            for j in i:
                if j != -1:
                    if len(tem) == 0:
                        tem=j
                    else:
                        tem.extend(j)
            result.append(tem.copy())
        print(result)



A = '43 460 3871 4698 8399 504 4421 7515 -1 4167 5727 -1 -1 3096 434 7389 2667 5661 1969 7815 4292 3006 9750 6693 -1 6906 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1'
root = buildTree(A)
s = Solution()
s.verticalOrderTraversal(root)

