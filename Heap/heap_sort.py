def heapify(A,n,index):
    i = index
    l = index * 2 + 1
    r = index * 2 + 2
    if l < n and A[index] > A[l]:
        index = l
    if r < n and A[index] > A[r]:
        index = r
    if index != i:
        A[index],A[i] = A[index],A[i]
        heapify(A,n,index)


def buildHeap(A,n):
    last = (n-1)//2
    while last > -1:
        heapify(A,n,last)
        last -= 1

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        n = len(A)
        ans = []
        buildHeap(A,n)
        ans.append(A[0])
        while n > -1:
            A[0],A[n-1] = A[n-1],A[0]
            heapify(A,n,0)
            ans.append(A[0])
            n -= 1
        return ans

