# Definition for a  binary tree node
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


def gen_sum(A, ans,total):
    if A.left and A.right:
        l_node = gen_sum(A.left, ans, total)
        r_node = gen_sum(A.right, ans, total)
        if (l_node.summ + r_node.summ + A.val) * 2 == total:
            ans[0] = 1
        return Node1(l_node.summ + r_node.summ + A.val)
    elif A.left:
        l_node = gen_sum(A.left, ans, total)
        summ = l_node.summ + A.val
        if total == summ * 2:
            ans[0] = 1
        return Node1(summ)
    elif A.right:
        r_node = gen_sum(A.right, ans, total)
        summ = r_node.summ + A.val
        if summ * 2 == total:
            ans[0] = 1
        return Node1(summ)
    else:
        if A.val * 2 == total:
            ans[0] = 1
        return Node1(A.val)

def getsum(A):
    if A is None:
        return 0
    else:
        return A.val+getsum(A.left)+getsum(A.right)

class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        summ = getsum(A)
        ans = [0]
        gen_sum(A, ans, summ)
        return ans[0]

s = Solution()
A = '106 -1 480 454 321 -1 -1 719 -1 -1'
root = buildTree(A)
ans = s.solve(root)
print(ans)


