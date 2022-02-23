def gen(A, v_arr, ans, curr, idx):
    n = len(A)
    if idx == n:
        ans.append(curr)
        return
    else:
        for i in range(n):
            if v_arr[i] == 0:
                curr1 = curr.copy()
                curr1.append(A[i])
                v_arr1 = v_arr.copy()
                v_arr1[i] = 1
                gen(A, v_arr1, ans, curr1, idx + 1)


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        n = len(A)
        v_arr = [0] * n
        idx = 0
        ans = []
        curr = []
        gen(A, v_arr, ans, curr, idx)
        return ans

if __name__ == '__main__':
    A = [1,2,2]
    s = Solution()
    ans = s.permute(A)
    print(ans)


