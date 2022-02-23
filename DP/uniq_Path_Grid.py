def uniquePathsWithObstacles(A):
        n = len(A)
        m = len(A[0])
        dp = []
        row = [-1] * (m + 1)
        for i in range(n + 1):
            dp.append(row.copy())
        for i in range(m+1):
            dp[0][i] = 0
        for i in range(n+1):
            dp[i][0] = 0
        if A[0][0] == 0:
            dp[1][1] = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                if dp[i][j] == -1:
                    if A[i-1][j-1] != 1:
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                    else:
                        dp[i][j] = 0
        print(dp)
        return dp[n][m]

A = [[1,0,0],[0,1,0],[0,0,0]]
ans = uniquePathsWithObstacles(A)
print(ans)


