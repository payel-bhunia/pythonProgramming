def mergeSort(arr, count, mod):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L, count, mod)
        mergeSort(R, count, mod)

        # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                count[0] += (len(L) - i) % mod
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        mod = 1000000007
        count = [0]
        mergeSort(A, count, mod)
        count[0] = count[0] % mod
        return count[0]

if __name__ == '__main__':
    A = [6, 12, 10, 17, 10, 22, 9, 19, 21, 31, 26, 8]
    s = Solution()
    ans = s.solve(A)
    print(ans)