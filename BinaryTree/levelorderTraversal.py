class Tree:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

    def levelorderTraversal(self, root):
        ans = []
        ans1 = []
        if root.data:
            ans.append(root)
            while len(ans) > 0:
                node = ans.pop(0)
                ans1.append( node.data)
                if node.left:
                    ans.append(node.left)
                if node.right:
                    ans.append(node.right)
        return ans1


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

    def level_order(self, root, level, ans):
        if root is not None:
            if len(ans) < level+1:
                ans.append([])
            ans[level].append(root.data)
            self.level_order(root.left,level+1,ans)
            self.level_order(root.right, level + 1, ans)
        else:
            return

    def vertical_order(self, root, ans, ht, key, offset):
        if root is not None:
            if (ans[key-offset][ht]) == -1:
                ans[key - offset][ht] = [root.data]
            else:
                ans[key - offset][ht].append(root.data)

            self.vertical_order(root.left, ans, ht + 1, key - 1, offset)
            self.vertical_order(root.right, ans, ht + 1, key + 1, offset)
        else:
            return

    def check_height_width(self, root, ht, key, key_height):
        if root is not None:
            key_height[0] = min(key_height[0], key)
            key_height[1] = max(key_height[1], key)
            key_height[2] = max(key_height[2], ht)
            self.check_height_width(root.left, ht + 1, key - 1, key_height)
            self.check_height_width(root.right, ht + 1, key + 1, key_height)
        else:
            return



if __name__ == "__main__":
    root = Tree(10)
    root.insert_node(12)
    root.insert_node(4)
    root.insert_node(7)
    root.insert_node(6)
    root.insert_node(9)
    root.insert_node(3)
    root.insert_node(11)
    root.insert_node(13)
    print(root.levelorderTraversal(root))
    level = 0
    ans = []
    root.level_order(root, level, ans)
    print(ans)
    key = 0
    ht = 0
    key_height = [1000000007,-1000000007 ,-1000000007]
    root.check_height_width(root, ht, key, key_height)
    max_height = key_height[2]
    size = key_height[1]-key_height[0]+1
    ans = []
    for i in range(size):
        temp = [-1] * (max_height+1)
        ans.append(temp)
        temp = []
    offset = key_height[0]
    print(ans, key, ht, offset,key_height)
    root.vertical_order(root, ans, ht, key, offset)
    print(ans)
    final = []
    for i in range(size):
        temp = []
        for j in range(max_height+1):
            if ans[i][j] != -1:
                temp += ans[i][j]
        final.append(temp)
    print(final)




