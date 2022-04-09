def calculatePath(i, j, memo):
    if i > -1 and j > -1:
        if memo[i][j] == -1:
            if i == 0 and j == 0:
                return 1
            else:
                memo[i][j] = calculatePath(i - 1, j, memo) + calculatePath(i, j - 1, memo)
        return memo[i][j]
    else:
        return 0


class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        if B == 1:
            return 1
        i = 0
        j = 0
        row = [0] * B
        memo = []
        for i in range(A):
            memo.append(row.copy())
        memo[0][0] = 1
        for i in range(1,B):
            memo[0][i]=memo[0][i-1]
        for i in range(1,A):
            memo[i][0] = memo[i-1][0]
        for i in range(1,A):
            for j in range(1,B):
                memo[i][j] = memo[i-1][j]+memo[i][j-1]
        return memo[A-1][B-1]

A = 15
B = 9
s = Solution()
print(s.uniquePaths(A,B))