import copy


def gen(A, i, ans, temp,hi,vi):
    # base condition
    if i == A:
        str = ''
        row = []
        for m in range(A):
            col = temp[-1]
            str = ''
            for n in range(A):
                if col == n:
                    str += 'Q'
                else:
                    str += '.'
            row.append(str)
        ans.append(row)
        return

    for k in range(A):
        if i != 0:
            prev_col = temp[-1]
            if hi[i] != 1 and vi[k] != 1 and k+1 != prev_col and k-1 != prev_col and k != prev_col:
                temp.append(k)
                #curr[i][k] = 'Q'
                hi[i] = 1
                vi[k] = 1
                gen(A, i + 1, ans, temp.copy(),hi.copy(),vi.copy())
                temp.pop()
                #curr[i][k] = '.'
                hi[i] = 0
                vi[k] = 0
        else:
            temp.append(k)
            #curr[i][k] = 'Q'
            hi[i] = 1
            vi[k] = 1
            gen(A, i + 1, ans, temp.copy(), hi.copy(), vi.copy())
            temp.pop()
            #curr[i][k] = '.'
            hi[i] = 0
            vi[k] = 0


class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, A):
        ans = []
        curr = []
        vi = [0] * A
        hi = [0] * A
        col = ['.'] * A
        for i in range(A):
            curr.append(col.copy())
        i = 0
        temp = []
        gen(A, i, ans, temp,vi,hi)
        return ans


if __name__ == '__main__':
    A = 8
    s = Solution()
    ans = s.solveNQueens(A)
    print(ans)