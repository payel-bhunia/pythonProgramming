class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        n = len(A)
        start = 0
        for i in range(n):
            if A[i] == 0:
                start += 1
            else:
                break
        if start == n:
            return [1]
        flag = 0
        for i in range(n-1,-1,-1):
            if A[i] < 9 and A[i] > 0:
                A[i] += 1
                return A[start:]
            elif A[i] == 9:
                A[i] = 0
                flag = 1
            else:
                A[i] = 1
                flag = 0
                if start>i:
                    start = i
                break
        if flag == 1:
            A.insert(0,1)
            return A
        else:
            return A[start:]
A = [3,0,6,4,0]
s=Solution()
ans = s.plusOne(A)
print(ans)