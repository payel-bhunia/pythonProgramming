# Definition for a  binary tree node
from collections import deque
class Node:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
         self.next = None

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
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        curr = root
        while curr is not None:
            first = None
            prev = None
            flag = 0
            while curr is not None:
                if prev is not None:
                    if curr.left:
                        prev.next = curr.left
                    elif curr.right:
                        prev.next = curr.right
                if curr.left and curr.right:
                    if flag == 0:
                        first = curr.left
                        flag = 1
                    curr.left.next = curr.right
                    prev = curr.right
                elif curr.left:
                    if flag == 0:
                        first = curr.left
                        flag = 1
                    prev = curr.left
                elif curr.right:
                    if flag == 0:
                        first = curr.right
                        flag = 1
                    prev = curr.right
                curr = curr.next
            if flag == 1:
                curr = first
            else:
                break
        return root


if __name__ == "__main__":
    t = 1
    for _ in range(0, t):
        s = '3 1 2 4 -1 -1 6'
        root = buildTree(s)
        k = Solution().connect(root)
        print(k)
