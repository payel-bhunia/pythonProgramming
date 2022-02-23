class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


    def insert_node(self,val):
        if val != "null":
            val = int(val)
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


    def preorder_traverse(self):
        ans = []
        if self.val:
            ans.append(self.val)
            if self.left:
                ans += self.left.preorder_traverse()
            if self.right:
                ans += self.right.preorder_traverse()
        return ans


class Solution:
    def isValidBST(self, root) -> bool:
        bool_val = True
        if root.val is not None:
            if root.left is not None:
                if root.left.val < root.val:
                    self.isValidBST(root.left)
                else:
                    bool_val = False
                    return bool_val
            if root.right is not None:
                if root.right.val > root.val:
                    self.isValidBST(root.right)
                else:
                    bool_val = False
                    return bool_val

        return bool_val



if __name__ == "__main__":
    s = Solution()
    root = TreeNode(5)
    root.insert_node(4)
    root.insert_node(6)
    root.insert_node('null')
    root.insert_node('null')
    root.insert_node(3)
    root.insert_node(7)
    print(root.preorder_traverse())
    print(s.isValidBST(root))

