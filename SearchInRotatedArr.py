class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, arr, target):
        # Write your code here.
        n = len(arr)
        start = 0
        end = n - 1

        while start < end:
            mid = start + (end - start) // 2
            if arr[mid] > arr[n - 1]:
                start = mid + 1
            elif arr[mid] < arr[n - 1]:
                end = mid
        if start == end:
            pivot = start
        #print(pivot, arr[pivot])
        if target >= arr[pivot] and target <= arr[n - 1]:
            start = pivot
            end = n - 1
        elif target > arr[n - 1] and target <= arr[pivot - 1]:
            start = 0
            end = pivot - 1
        else:
            return -1
        #print(start, end)
        while start < end:
            mid = start + (end - start) // 2
            if arr[mid] > target:
                end = mid - 1
            elif arr[mid] < target:
                start = mid + 1
            else:
                return mid
        if start == end:
            if arr[start] == target:
                return start
            else:
                return -1
        else:
            return -1



if __name__ == "__main__":
    s = Solution()
    A = [4, -1, 0, 2, 3 ]
    B = 1
    n = s.search(A, B)
    print(n)
