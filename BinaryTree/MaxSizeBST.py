# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


    def insert_node(self, val):
        if self.val:
            if self.val <= val:
                if self.right is None:
                    self.right = TreeNode(val)
                else:
                    self.right.insert_node(val)
            else:
                if self.left is None:
                    self.left = TreeNode(val)
                else:
                    self.left.insert_node(val)
        else:
            self.val = val
class Node:
    def __init__(self,isBST,size,maxx,minn):
        self.isBST = isBST
        self.size = size
        self.maxx = maxx
        self.minn = minn
        #self.maxBST = maxBST
def populateNode(A,max_BST):
    if A.right is None and A.left is None:
        max_BST[0] = max(max_BST[0],1)
        return Node(True,1,A.val,A.val)
    elif A.right is None:
        n = populateNode(A.left,max_BST)
        isBST = A.val > n.maxx and n.isBST
        if isBST:
            max_BST[0] = max(max_BST[0], n.size+1)
        return Node(isBST,n.size+1,A.val,n.minn)
    elif A.left is None:
        n = populateNode(A.right,max_BST)
        isBST = A.val < n.minn and n.isBST
        if isBST:
            max_BST[0] = max(max_BST[0], n.size+1)
        return Node(isBST,n.size+1,n.maxx,A.val)
    else:
        right = populateNode(A.right,max_BST)
        left = populateNode(A.left,max_BST)
        isBST = A.val > left.maxx and A.val < right.minn and right.isBST and left.isBST
        if isBST:
            max_BST[0] = max(max_BST[0], right.size+left.size+1)
        return Node(isBST,right.size+left.size+1,right.maxx,left.minn)
class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        max_BST = [0]
        populateNode(A,max_BST)
        return max_BST[0]

if __name__ == "__main__":
    root = TreeNode(10)
    root.insert_node(12)
    root.insert_node(4)
    root.insert_node(7)
    root.insert_node(6)
    root.insert_node(9)
    root.insert_node(3)
    root.insert_node(11)
    root.insert_node(13)
    s = Solution()
    ans = s.solve(root)
    print(ans)


