class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        n = len(A)
        i = 0
        while i < n:
            if A[i]>0 and A[i] < n+1:
                if A[i] != i + 1 and A[A[i]-1] != A[i]:
                    A[A[i] - 1], A[i] = A[i], A[A[i] - 1]
                else:
                    i += 1
            else:
                i += 1
        for i in range(n):
            if A[i] != i + 1:
                return i + 1
            if i == n-1 and A[i] == n:
                return n+1


if __name__ == '__main__':
    A = [-3,-2, 1, 3, 1,2,4,6]
    s= Solution()
    n = s.firstMissingPositive(A)
    print(n)