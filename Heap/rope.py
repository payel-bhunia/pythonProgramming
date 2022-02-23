# User function Template for python3
def heapify(arr, index):
    n = len(arr)
    minn = index
    l = 2 * index + 1
    r = 2 * index + 2
    if l < n:
        if arr[l] < arr[index]:
            index = l
    if r < n:
        if arr[r] < arr[index]:
            index = r
    if index != minn:
        arr[index], arr[minn] = arr[minn], arr[index]
        heapify(arr, index)


def buildMinHeap(arr):
    n = len(arr)
    index = n // 2 - 1
    while index > -1:
        heapify(arr, index)
        index -= 1


def deleteRoot(arr):
    arr[0] = arr[-1]
    arr.pop()
    heapify(arr, 0)

def heapifyBottomTop(A,index):
    if index == 0:
        return
    parent = (index-1)//2
    if A[parent] > A[index]:
        A[parent],A[index] = A[index],A[parent]
        heapifyBottomTop(A,parent)
    else:
        return




class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        cost = 0
        buildMinHeap(A)
        while (n > 2):
            x = A[0]
            deleteRoot(A)
            y = A[0]
            deleteRoot(A)
            z = x + y
            A.append(z)
            heapifyBottomTop(A,n-2)
            # print(arr)
            cost += z
            # print(cost)
            n -= 1
        if n == 2:
            cost += A[0] + A[1]
        return cost

if __name__ == '__main__':
    A = [18, 3, 16, 10, 17, 1, 5, 7, 13, 15]
    s = Solution()
    ans = s.solve(A)
    print(ans)