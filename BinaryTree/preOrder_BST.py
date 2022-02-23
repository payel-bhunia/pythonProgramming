# User function Template for python3
class Info:
    def __init__(self, isBST, maxx, minn):
        self.isBST = isBST
        self.maxx = maxx
        self.minn = minn


def checkBST1(root):
    if root.left != None and root.right != None:
        lInfo = checkBST(root.left)
        rInfo = checkBST(root.right)
        curIsBST = lInfo.isBST and rInfo.isBST and root.data > lInfo.maxx and root.data < rInfo.minn
        currMax = rInfo.maxx
        currMin = lInfo.minn
        return Info(curIsBST,currMax,currMin)
    elif root.left != None:
        lInfo = checkBST(root.left)
        curIsBST = lInfo.isBST and root.data > lInfo.maxx
        currMax = root.data
        currMin = lInfo.minn
        return Info(curIsBST,currMax,currMin)
    elif root.right != None:
        rInfo = checkBST(root.right)
        curIsBST = rInfo.isBST and root.data < rInfo.minn
        currMax = rInfo.maxx
        currMin = root.data
        return Info(curIsBST,currMax,currMin)
    else:
        return Info(True,root.data,root.data)


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def buildTree(arr,N):
    if N > 1:
        root = Node(arr[0])
        flag = 0
        for i in range(1,N):
            if arr[i] > root.data:
                flag = 1
                temp = arr[1:i]
                root.left = buildTree(temp, len(temp))
                root.right = buildTree(arr[i:], N-len(temp)-1)
                break
        if flag == 0:
            temp = arr[1:N]
            root.left = buildTree(temp, len(temp))
            root.right = buildTree([], 0)
        return root
    elif N == 1:
        root = Node(arr[0])
        root.left = None
        root.right = None
        return root
    else:
        return None

def check_BST(root, max_l, min_l):
    if root == None:
        return True
    else:
        if root.data >= max_l or root.data <= min_l:
            return False
        else:
            return check_BST(root.left, root.data, min_l) and check_BST(root.right, max_l, root.data)
class Solution:
    def canRepresentBST(self, arr, N):
        root = buildTree(arr, N)
        max_l = 1000000007
        min_l = -1000000007

        return check_BST(root, max_l, min_l)


# {
#  Driver Code Starts
# Initial Template for Python 3

import sys

sys.setrecursionlimit(10 ** 6)

if __name__ == '__main__':
    t = 1
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])

        ob = Solution()
        print(ob.canRepresentBST(arr, N))
# } Driver Code Ends