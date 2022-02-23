import copy
def gen(n, vv, hv, cv1, cv2, curr, ans, idx,count):
    # base condition
    if count == n:
        ans.append(curr)
        return

    for i in range(idx, n):
        if hv[i] == 0:
            for j in range(n):
                if vv[j] == 0:
                    if cv1[i + j] == 0 and cv2[j - i + n - 1] == 0:
                        hv[i] = 1
                        vv[j] = 1
                        #cv11 = cv1.copy()
                        cv1[i + j] = 1
                        #cv22 = cv2.copy()
                        cv2[j - i + n - 1] = 1
                        s = ['.'] * n
                        s[j] = 'Q'
                        st = ''.join(map(str, s))
                        curr1 = curr.copy()
                        curr1.append(st)
                        gen(n, vv.copy(), hv.copy(), cv1.copy(), cv2.copy(), curr1, ans, i + 1, count+1)
                        hv[i] = 0
                        vv[j] = 0
                        # cv11 = cv1.copy()
                        cv1[i + j] = 0
                        # cv22 = cv2.copy()
                        cv2[j - i + n - 1] = 0


class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, A):
        ans = []
        curr = []
        vv = [0] * A
        hv = [0] * A
        cv1 = [0] * (2 * A - 1)
        cv2 = [0] * (2 * A - 1)
        idx = 0
        ans = []
        count = 0
        gen(A, vv, hv, cv1, cv2, curr, ans, idx,count)
        return ans



if __name__ == '__main__':
    A = 4
    s = Solution()
    ans = s.solveNQueens(A)
    print(ans)