class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None

    def print_tree(self):
        if self.left != None:
            self.left.print_tree()
        print(self.data)
        if self.right != None:
            self.right.print_tree()

    def insert_node(self,val):
        if self.data:
            if self.data <= val:
                if self.right == None:
                    self.right = Node(val)
                else:
                    self.right.insert_node(val)
            else:
                if self.left == None:
                    self.left = Node(val)
                else:
                    self.left.insert_node(val)
        else:
            self.data = val

    def inorder_traverse(self):
        ans =[]
        print("root data", self.data)
        if self.data:
            if self.left != None:
                ans = self.left.inorder_traverse()
            ans.append(self.data)
            #print(ans)
            if self.right != None:
                ans += self.right.inorder_traverse()
        return ans

    def preorder_traverse(self):
        ans = []
        if self.data:
            ans.append(self.data)
            if self.left:
                ans += self.left.preorder_traverse()
            if self.right:
                ans += self.right.preorder_traverse()
        return ans

    def postorder_traverse(self):
        ans = []
        if self.data:

            if self.left:
                ans = self.left.postorder_traverse()
            if self.right:
                ans += self.right.postorder_traverse()
            ans.append(self.data)
        return ans



if __name__ == "__main__":
    root = Node(10)
    root.insert_node(11)
    root.insert_node(4)
    root.insert_node(7)
    root.insert_node(6)
    root.insert_node(12)
    root.print_tree()
    print(root.inorder_traverse())
    print(root.preorder_traverse())
    print(root.postorder_traverse())
