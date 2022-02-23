def isFeasible(A, B, mid):
    summ = 0
    student = 1
    for i in range(len(A)):
        if summ + A[i] <= mid:
            summ += A[i]
        else:
            student += 1
            summ = A[i]
    return student <= B


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def books(self, A, B):
        n = len(A)
        if n < B:
            return -1
        elif n == B:
            return max(A)
        else:
            low = max(A)
            high = sum(A)
            while low <= high:
                mid = (low + high) // 2
                if isFeasible(A, B, mid):
                    res = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return res

if __name__ == "__main__":
    A = [12, 34, 67,90]
    B = 2
    s = Solution()
    ans = s.books(A,B)
    print(ans)



