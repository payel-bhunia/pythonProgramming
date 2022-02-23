def recur(A,B,size,summ,ind):
    if size == B:
        if summ <= 1000:
            return 1
        else:
            return 0

    if ind == len(A) and size < B:
        return 0
    if summ > 1000:
        return 0
    if summ < 0:
        return 0
    return recur(A,B,size+1,summ+A[ind],ind+1) + recur(A,B,size,summ,ind+1)

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        size = 0
        summ = 0
        n = len(A)
        ind = 0
        ans = 0
        if n == B:
            if sum(A) > 1000:
                return 0
            else:
                return 1
        elif B > n:
            return 0
        else:
            if min(A) > 1000:
                return 0
            else:
                ans = recur(A,B,size,summ,ind)
                return ans


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    B = 5
    s = Solution()
    ans = s.solve(A,B)
    print(ans)