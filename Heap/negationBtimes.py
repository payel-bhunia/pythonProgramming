# User function Template for python3
def heapify(arr, n, index):
    largest = index
    l = 2 * index + 1
    r = 2 * index + 2
    if l < n:
        if arr[l] < arr[largest]:
            largest = l
    if r < n:
        if arr[r] < arr[largest]:
            largest = r
    if index != largest:
        arr[index], arr[largest] = arr[largest], arr[index]
        heapify(arr, n, largest)


def buildMinHeap(arr, n):
    index = n // 2 - 1
    while index > -1:
        heapify(arr, n, index)
        index -= 1


def deleteRoot(arr, n):
    x = arr[0]
    arr[0] = arr[n - 1]
    arr.pop()
    buildMinHeap(arr, n - 1)
    return x


def insertHeap(arr, n, val):
    arr.append(val)
    buildMinHeap(arr, n + 1)


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        b = B
        if B < n // 2:
            while B > 0:
                buildMinHeap(A, n)
                A[0], A[n - 1] = A[n - 1], A[0]
                A[n - 1] = -1 * A[n - 1]
                B -= 1
            return sum(A)
        else:
            A.sort()
            i = 0
            while B > 0:
                if i < n:
                    if A[i] < 0:
                        A[i] = -1 * A[i]
                        B -= 1
                        i += 1
                    else:
                        break
                else:
                    break

            if B > 0:
                min_ele = A[0]
                index = 0
                for i in range(1, n):
                    if A[i] < min_ele:
                        min_ele = A[i]
                        index = i
                while B > 0:
                    A[index] = (-1) * A[index]
                    B -= 1
            return sum(A)



if __name__ == '__main__':
    A = [57, 3, -14, -87, 42, 38, 31, -7, -28, -61]
    B = 10
    s = Solution()
    ans = s.solve(A,B)
    print(ans)