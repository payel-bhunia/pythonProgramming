# Your task is to complete this function
def evalExpr(root):
    if root == None:
        return 0
    elif isExp(root.data):
        leftval = evalExpr(root.left)
        rightval = evalExpr(root.right)
        if root.data == '+':
            return leftval + rightval
        elif root.data == '-':
            return leftval - rightval
        elif root.data == '*':
            return leftval * rightval
        else:
            return leftval // rightval
    else:
        return int(root.data)


class Solution:
    # function should return an integer denoting the required answer
    def evalTree(self, root):
        ans = evalExpr(root)
        return ans

        # Code here


# {
#  Driver Code Starts
class node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


def isExp(s):
    if s == "+" or s == "-" or s == "*" or s == "/":
        return True
    return False


if __name__ == '__main__':
    t = 1
    for i in range(t):
        n = 9
        arr = ['/', '/', '-', '1', '-', '16', '9', '5', '11']
        q = []
        p = 0
        root = node(arr[p])
        q.append(root)
        p = 1
        while q != []:
            f = q.pop(0)
            if isExp(f.data):
                l = node(arr[p])
                p += 1
                r = node(arr[p])
                p += 1
                f.left = l
                f.right = r
                q.append(l)
                q.append(r)

        # inorder(root)
        # print ''
        print(Solution().evalTree(root))

# } Driver Code Ends