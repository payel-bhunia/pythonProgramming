import sys
class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        ans_i_max = -10**9
        ans_i_min = sys.maxsize
        print(ans_i_min)
        ans_j_max = -10**9
        ans_j_min = 10**9
        for i in range(len(A)):
            ans_i_max = max(ans_i_max,A[i]+i)
            ans_j_max = max(ans_j_max,A[i]-i)
            ans_i_min = min(ans_i_min, A[i]+i)
            ans_j_min = min(ans_j_min, A[i]-i)
        max_diff_i = ans_i_max - ans_i_min
        max_diff_j = ans_j_max - ans_j_min
        return max(max_diff_i,max_diff_j)


if __name__ == '__main__':
    A = [-70, -64, -6, -56, 64, 61, -57, 16, 48, -98]
    s= Solution()
    n = s.maxArr(A)
    print(n)