class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        m = len(B)
        row = [-1] * (m+1)
        dp = []
        for i in range(n+1):
            dp.append(row.copy())
        i = 0
        j = 0
        while j < m:
            dp[i][j] = 0
            j += 1
        j = 0
        while i < n:
            dp[i][j] = 0
            i += 1

        for i in range(1,n+1):
            for j in range(1,m+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[n][m]

A = "beb"
B = "abeb"
s= Solution()
ans = s.solve(A,B)
print(ans)