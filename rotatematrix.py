class Solution:
    # @param A : list of list of integers
    def solve(self, A):
        n = len(A)
        if n == 1:
            return A
        ans = []
        for i in range(n):
            ans.append([0] * n)
        for i in range(n):
            for j in range(n):
                ans[j][n-1-i] = A[i][j]
        return ans

if __name__ == '__main__':
    A = [[1, 2], [3, 4]]
    s = Solution()
    n = s.solve(A)
    print(n)


