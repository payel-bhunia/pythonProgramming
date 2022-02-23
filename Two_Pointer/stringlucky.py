class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        score_Mindy = [0]*n
        if A[0]==0:
            score_Mindy[0] = B[0]
        for i in range(1,n):
            if A[i] == 0:
                score_Mindy[i] = B[i]+score_Mindy[i-1]
            else:
                score_Mindy[i] = score_Mindy[i-1]
        print(score_Mindy)
        max_M = score_Mindy[-1]
        end = 0
        while end <n:
            if A[end] == 0:
                end += 1
            else:
                break
        if end == n:
            return max_M
        curr1 = score_Mindy[end]
        curr = max_M
        while end < n:
            if A[end] == 0:
                curr -= B[end]
                #curr1 -= B[end]
                if curr <= max_M:
                    curr = max_M
                    curr1 = score_Mindy[end]
            elif A[end] == 1:
                curr += B[end]
                curr1 += B[end]
                max_M = max(max_M,curr1)
            end += 1
        return max(max_M,curr1)


if __name__ == '__main__':
    #A = [1,0,1,0,1]
    #B = [18,7,14,3,27]
    #A = [0, 0, 1, 0, 1]
    #B = [41, 47, 11, 20,33]
    A =[1,0,1]
    B = [30,12,8]
    s = Solution()
    print(s.solve(A,B))