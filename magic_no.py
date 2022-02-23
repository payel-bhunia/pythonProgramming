def power(A, n):
    if n == 0:
        return 1
    ans = 1
    while(n > 0):
        ans = ans * A
        n -= 1
    return ans

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        B = A
        s = ''
        n = 0
        ans = 0
        while B > 0:
            s = str(B%2) + s
            B = B//2
            n += 1
        for i in range(n):
            if s[i] == '1':
                ans += power(5, n-i)
        return ans


if __name__ == '__main__':
    A = 10
    s = Solution()
    print(s.solve(A))
