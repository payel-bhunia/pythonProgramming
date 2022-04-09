class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        mod = 10 ** 9 + 7
        ans = 0

        for i in range(32):
            for j in range(n - 1, -1, -1):
                bit = (A[j] >> i) & 1
                if bit == 1:
                    ans += (n - j) * (2 ** i)
        return ans % mod
A = [1,2,3]
s = Solution()
ans = s.solve(A)
print(ans)
