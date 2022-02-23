# User function Template for python3

'''
# Node class

class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

'''


def findRoot(inorder, preorder, n):
    if n > 0:
        root = Node(preorder[0])
        if n >= 1:
            for i in range(n):
                if inorder[i] == root.data:
                    rightIn = inorder[i + 1:]
                    leftIn = inorder[0:i]
                    break
            sz = len(leftIn)
            leftPre = preorder[1:sz + 1]
            rightPre = preorder[sz + 1:]
            root.left = findRoot(leftIn, leftPre, sz)
            root.right = findRoot(rightIn, rightPre, len(rightIn))
        #elif n == 2:
        #    if inorder[0] == root.data:
        #        root.left = None
        #        root.right = Node(inorder[1])
        #    else:
        #        root.left = Node(inorder[0])
        #        root.right = None
        #elif n == 3:
        #    root.left = Node(inorder[0])
        #    root.right = Node(inorder[2])
        elif n == 1:
            root.left = None
            root.right = None
        return root
    else:
        return None


class Solution:
    def buildtree(self, inorder, preorder, n):
        root = findRoot(inorder, preorder, n)
        return root
        # code here
        # build tree and return root node


# {
#  Driver Code Starts
# Initial Template for Python 3

class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


def printPostorder(n):
    if n is None:
        return
    printPostorder(n.left)
    printPostorder(n.right)
    print(n.data, end=' ')


if __name__ == "__main__":
    t = 1
    for _ in range(t):
        n = int(input())
        inorder = [int(x) for x in input().split()]
        preorder = [int(x) for x in input().split()]

        root = Solution().buildtree(inorder, preorder, n)
        printPostorder(root)
        print()

# } Driver Code Ends