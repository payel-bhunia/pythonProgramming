class Solution:
    def countMinSquares(self, A):
        dp = [-1] * (A + 1)
        for i in range(1, A + 1):
            dp[i] = i
            x = 1
            while x * x <= i:
                val = x * x
                dp[i] = min(dp[i], dp[i - val] + 1)
                x += 1
        return dp[i]

A = 12
s = Solution()
print(s.countMinSquares(A))


