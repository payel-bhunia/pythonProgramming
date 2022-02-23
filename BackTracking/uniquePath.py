def check_matrix(A, x, y, count, visited, ans):
    if (x >= len(A) or x < 0) or (y >= len(A[0]) or y < 0):
        return
    if A[x][y] == 2:
        if visited-1 == count:
            ans[0] += 1
        else:
            return
    elif A[x][y] != -1:
        state = A[x][y]
        A[x][y] = -1
        check_matrix(A.copy(), x + 1, y, count, visited+1, ans)
        check_matrix(A.copy(), x-1, y, count, visited+1, ans)
        check_matrix(A.copy(), x, y+1, count, visited+1, ans)
        check_matrix(A.copy(), x, y-1, count, visited+1, ans)
        A[x][y] = state
    else:
        return




class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        count = 0
        x = 0
        y = 0
        n = len(A)
        m = len(A[0])
        ans = [0]
        visited = 0
        for i in range(n):
            for j in range(m):
                if A[i][j] == 1:
                    x = i
                    y = j
                elif A[i][j] == 0:
                    count += 1
        check_matrix(A, x, y, count, visited, ans)
        return ans[0]

if __name__ == '__main__':
    A = [[2, -1],[0, 0],[-1, 1]]
    s = Solution()
    ans = s.solve(A)
    print(ans)