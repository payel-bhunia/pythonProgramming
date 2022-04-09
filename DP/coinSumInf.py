
class Solution:
    def coinchange2(self, A, B):
        n = len(A)
        mod = 1000007
        dp = []
        prev = [0] * (B + 1)

        curr = [-1] * (B + 1)
        i = 0
        j = 0
        prev[0] = 1
        curr[0] = 1
        for i in range(1, n + 1):
            for j in range(1, B + 1):
                if j >= A[i - 1]:
                    curr[j] = (prev[j] + curr[j - A[i - 1]]) % mod
                else:
                    curr[j] = prev[j] % mod
            prev = curr.copy()
        return curr[B] % mod


A = [1, 2, 3]
B = 4
s = Solution()
ans = s.coinchange2(A, B)
print(ans)