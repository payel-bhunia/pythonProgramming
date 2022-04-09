def isGoodBase(n,k,i):
    val = (k**i-1)//(k-1)
    if val == n:
        return 0
    elif val > n:
        return 1
    else:
        return -1

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        n = int(A)
        low = 2
        high = n-1
        for i in range(64,-1,-1):
            if 1<<i <= n:
                max_size = i+1
                break
        res = -1
        for i in range(max_size,1,-1):
            l = 2
            r = n-2
            while l<=r:
                m = l+(r-l)//2
                if (m**i) <= n:
                    val = isGoodBase(n, m, i+1)
                    if val == 0:
                        res = m
                        break
                    elif val > 0:
                        r = m-1
                    else:
                        l = m+1
                else:
                    r = m-1
        if res == -1:
            return n-1
        else:
            return res




A = '13'
s = Solution()
print(s.solve(A))