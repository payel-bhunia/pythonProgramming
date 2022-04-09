class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        n = len(A)
        #print(A.index(1))
        i = 0
        while i < n:
            if A[i] > 0 and A[i] < n + 1:
                if A[i] != i + 1 and A[A[i] - 1] != A[i]:
                    temp = A[i]
                    A[i] = A[A[i] - 1]
                    A[temp - 1] = temp
                else:
                    i+=1
            else:
                i+=1
        #print(A)
        for i in range(n):
            if A[i] != i + 1:
                return i + 1
            if i == n - 1 and A[i] == n:
                return n + 1


if __name__ == '__main__':
    A = [3,4,-1,1]
    s= Solution()
    n = s.firstMissingPositive(A)
    A.sort()
    print(A)
    print(n)