class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_BT(self, rt, val):
        if rt is None:
            rt = TreeNode(val)
            return 1
        else:
            if self.insert_BT(rt.left, val) == 1:
                return 1
            else:
                self.insert_BT(rt.left, val) == 1



