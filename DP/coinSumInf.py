def dp(A,B,ans):
    if B == 0:
        return 1
    if ans[B] == 0:
        for i in A:
            if i <= B:
                ans[B] += dp(A, B - i, ans)
    return ans[B]


class Solution:
    def coinchange2(self, A, B):
        ans = [0] * (B + 1)
        dp(A, B, ans)
        return ans[B]

A = [1,2,3]
B = 4
s = Solution()
ans = s.coinchange2(A,B)
print(ans)