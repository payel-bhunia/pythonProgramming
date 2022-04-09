def heapify(A,n,index):
    i = index
    l = index*2 + 1
    r = index*2 + 2
    if l < n:
        if A[index] > A[l]:
            index = l
    if r < n:
        if A[index] > A[r]:
            index = r
    if index != i:
        A[index],A[i] = A[i],A[index]
        heapify(A, n, index)



class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        last = n//2 - 1
        while last > -1:
            heapify(A,n,last)
            last -= 1
        while A[0] < 0:
            if B > 0:
                A[0] = A[0] * (-1)
                heapify(A, n, 0)
                B -= 1
            else:
                break
        if A[0] > 0 and B > 0:
            if B%2 == 1:
                A[0] = (-1) * A[0]
        return sum(A)


if __name__ == '__main__':
    A = [57, 3, -14, -87, 42, 38, 31, -7, -28, -61]
    B = 10
    s = Solution()
    ans = s.solve(A,B)
    print(ans)