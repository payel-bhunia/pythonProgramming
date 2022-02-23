class Tree:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

    def insert_node(self, val):
        if self.data:
            if self.data <= val:
                if self.right is None:
                    self.right = Tree(val)
                else:
                    self.right.insert_node(val)
            else:
                if self.left is None:
                    self.left = Tree(val)
                else:
                    self.left.insert_node(val)
        else:
            self.data = val

    def top_view(self, root, dic, wd,ht):
        if root is None:
            return
        else:
            if wd not in dic:
                dic[wd] = (root.data,ht)
            else:
                if ht < dic[wd][1]:
                    dic[wd] = (root.data, ht)
            self.top_view(root.left, dic, wd - 1,ht+1)
            self.top_view(root.right, dic, wd + 1, ht+1)

    def right_view(self, root , dic, ht):
        if root is None:
            return
        else:
            if ht not in dic:
                dic[ht] = root.data
            self.right_view(root.right, dic, ht+1)
            self.right_view(root.left, dic, ht + 1)

    def get_height(self,root, dic):
        if root is None:
            return 0
        else:
            lH = self.get_height(root.left,dic)
            rH = self.get_height(root.right,dic)
            dic[root.data] = max(lH, rH) + 1
            return dic[root.data]

    def isBalanced(self, root, dic):
        if root is None:
            return True
        if root.left is not None:
            hL = dic[root.left.data]
        else:
            hL = 0
        if root.right is not None:
            hR = dic[root.right.data]
        else:
            hR = 0
        if abs(hL-hR) > 1:
            return False
        else:
            return self.isBalanced(root.left, dic) and self.isBalanced(root.right, dic)



if __name__ == "__main__":
    root = Tree(10)
    root.insert_node(12)
    root.insert_node(14)
    root.insert_node(5)
    root.insert_node(3)
    root.insert_node(2)
    ht = 0
    wd = 0
    dic = dict()
    ans = []
    root.top_view(root, dic, wd, ht)
    for key in dic:
        ans.append(dic[key][0])
    print(ans)
    dic2 = dict()
    ht = 0
    root.right_view(root, dic2, ht)
    ans1 = []
    for key in dic2:
        ans1.append(dic2[key])
    print(ans1)
    ht = 0
    dic3 = dict()
    root.get_height(root,dic3)
    print(dic3)
    print(root.isBalanced(root, dic3))


