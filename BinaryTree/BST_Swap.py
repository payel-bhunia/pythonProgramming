# Definition for a  binary tree node
from collections import deque

class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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


class Solution:
    def recoverTree(self, A):
        curr = A
        i = -1
        mid = -1
        last = -1
        prev = None
        chk = None
        while curr is not None:
            if curr.left is None:
                if prev is not None and prev.val > curr.val:
                    if i == -1:
                        mid = curr.val
                        i = prev.val
                    else:
                        last = curr.val
                prev = curr
                curr = curr.right
            else:
                chk = curr.left
                while chk.right is not None and chk.right != curr:
                    chk = chk.right
                if chk.right is None:
                    chk.right = curr
                    curr = curr.left
                elif chk.right == curr:
                    if curr.val < chk.val:
                        if i == -1:
                            mid = curr.val
                            i = chk.val
                        else:
                            last = curr.val
                    prev = curr
                    chk.right = None
                    curr = curr.right

        if last != -1:
            return [i, last]
        else:
            return [i, mid]


if __name__ == "__main__":
    t = 1
    for _ in range(0, t):
        s = '3 1 2'
        root = buildTree(s)
        k = Solution().recoverTree(root)
        print(k)