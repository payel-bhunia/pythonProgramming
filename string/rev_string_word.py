class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        ans = ''
        l = 0
        r = 0
        n = len(A)
        while r < n:
            if A[r] ==  ' ':
                if A[l] != ' ':
                    if ans == '':
                        ans = A[l:r]
                    else:
                        ans = A[l:r] + ' ' + ans
                l = r+1
                r = r+1
            else:
                r += 1
        if r == n and l<r:
            ans = A[l:r] + ' ' + ans
        return ans

if __name__ == "__main__":
    A = ' crulgzfkif gg ombt vemmoxrgf qoddptokkz op xdq hv    '
    s = Solution()
    ans = s.solve(A)
    print('$'+ans+'$')

    91495447







