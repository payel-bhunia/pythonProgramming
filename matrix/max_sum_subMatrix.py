# User function Template for python3

class Solution:
    def maxSubMatrixSumQueries(self, mat, n, m, queries, q):
        # code here
        pref_mx = [[0 for j in range(m)] for i in range(n)]
        pref_mx[0][0] = mat[0][0]
        for i in range(1, m):
            pref_mx[0][i] = pref_mx[0][i - 1] + mat[0][i]
        print(pref_mx)
        for i in range(1, n):
            pref_mx[i][0] = pref_mx[i - 1][0] + mat[i][0]
        print(pref_mx)
        for i in range(1, n):
            for j in range(1, m):
                pref_mx[i][j] = pref_mx[i - 1][j - 1] + mat[i][j] + mat[i - 1][j] + mat[i][j - 1]
        print(pref_mx)
        return [0] * q

1 2 3 9
4 5 6 2
8 3 2 6
1 3 6 15
4 9 15 17
8 11 13 19
# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = 1
    while tc > 0:
        n, m = list(map(int, input().strip().split()))
        inputLine = list(map(int, input().strip().split()))
        mat = [[0 for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                mat[i][j] = inputLine[i * n + j]
        q = int(input())
        inputLine = list(map(int, input().strip().split()))
        queries = [[0 for j in range(2)] for i in range(q)]
        for i in range(q):
            for j in range(2):
                queries[i][j] = inputLine[i * 2 + j]

        ob = Solution()
        mat= [[1,2,3,9],[4, 5, 6, 2],[8, 3, 2, 6]]
        ans = ob.maxSubMatrixSumQueries(mat, n, m, queries, q)
        for xx in ans:
            print(xx, end=" ")
        print()
        tc -= 1

# } Driver Code Ends