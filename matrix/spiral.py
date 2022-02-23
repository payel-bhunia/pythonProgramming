class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        m = len(A)
        n = len(A[0])
        k = 0
        l = 0
        ans = []
        while k < m and l < n:
            for i in range(l,n):
                ans.append(A[k][i])
            k+=1
            for i in range(k,m):
                ans.append(A[i][n-1])
            n -= 1
            if k<m:
                for i in range(n-1,l-1,-1):
                    ans.append(A[m-1][i])
                m-=1
            if l<n:
                for i in range(m-1,k-1,-1):
                    ans.append(A[i][l])
                l+=1
        return ans


if __name__ == "__main__":
    A = [[1,2],[3,4]]
    s = Solution()
    ans = s.spiralOrder(A)
    print(ans)