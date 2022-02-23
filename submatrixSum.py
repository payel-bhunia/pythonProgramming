class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @param D : list of integers
    # @param E : list of integers
    # @return a list of integers
    def solve(self, A, B, C, D, E):
        n = len(A)
        m = len(A[0])
        pref = []
        for i in range(n):
            pref.append([A[i][0]] * m)
        for i in range(n):
            for j in range(1, m):
                pref[i][j] = pref[i][j - 1] + A[i][j]
        for i in range(1, n):
            for j in range(m):
                pref[i][j] = pref[i - 1][j] + pref[i][j]
        q = len(B)
        ans = []
        for it in range(q):

            k = D[it] - 1
            l = E[it] - 1
            i = B[it] - 1
            j = C[it] - 1
            sum = pref[k][l]
            if i != 0:
                sum -= pref[i - 1][l]
            if j != 0:
                sum -= pref[k][j - 1]
            if i != 0 and j != 0:
                sum += pref[i - 1][j - 1]
            ans.append(sum)
        return ans


if __name__ == '__main__':
    A = [[5, 17, 100, 11],
         [0, 0, 2, 8]]
    B = [1, 1]
    C = [1, 4]
    D = [2, 2]
    E = [2, 4]
    s= Solution()
    n = s.solve(A, B, C, D, E)
    print(n)