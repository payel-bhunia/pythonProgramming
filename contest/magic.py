class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        mod = 1000000007
        n = len(A)
        mid = n//2
        max_sum = 0
        min_sum = 0
        for i in range(mid):
            min_sum += A[i]
        for i in range(mid,n):
            max_sum += A[i]
        max_magic = abs(max_sum - min_sum)
        sum1 = 0
        sum2 = 0
        A.sort()
        for i in range(n):
            if i&1 == 0:
                sum1 += A[i]
            else:
                sum2 += A[i]
        min_magic = abs(sum1-sum2)
        return [max_magic%mod,min_magic%mod]


if __name__ == '__main__':
    tc = 1
    while tc > 0:
        n = 10
        arr = [-98,-97,-64,-52,12,15,23,52,54,85]
        ob = Solution()
        ans = ob.solve(arr)
        for xx in ans:
            print(xx, end=" ")
