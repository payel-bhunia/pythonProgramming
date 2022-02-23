class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


def preOrder(ans, root):
    if root is None:
        return
    else:
        ans.append(root.data)
        preOrder(ans, root.left)
        preOrder(ans, root.right)


class Solution:
    def sortedArrayToBST(self, nums):
        # code here
        if len(nums) == 0:
            return
        else:
            mid = len(nums) // 2
            root = Node(nums[mid])
            root.left = self.sortedArrayToBST(nums[:mid])
            root.right = self.sortedArrayToBST(nums[mid + 1:])
            return root



# {
#  Driver Code Starts
if __name__ == '__main__':
    T = 1
    for i in range(T):
        n = 5
        nums = [1,2,3,4]
        obj = Solution()
        root = obj.sortedArrayToBST(nums)
        ans = []
        preOrder(ans, root)
        for _ in ans:
            print(_, end=" ")
        print()

# } Driver Code Ends