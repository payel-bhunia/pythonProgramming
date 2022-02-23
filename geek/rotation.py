# User function Template for python3
class Solution:
    def findKRotation(self, arr, n):
        A = arr
        start = 0
        end = n - 1
        while start <= end:
            mid = start + (end - start) // 2
            if mid < n - 1:
                if A[mid] > A[mid + 1]:
                    return mid + 1
                else:
                    if A[mid] > A[-1]:
                        start = mid + 1
                    else:
                        end = mid - 1
            else:
                if A[mid - 1] < A[mid]:
                    return 0
                else:
                    return n - 1
        return start

        # code here


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':

    tc = 1
    while tc > 0:
        n = int(input())
        a = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findKRotation(a, n)
        print(ans)
        tc = tc - 1

# } Driver Code Ends