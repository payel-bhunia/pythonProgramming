# User function Template for python3

# Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self, arr, n, s):
        summ = 0
        start = 0
        end = 0
        while start <= end and end <= n:
            while summ > s:
                summ -= arr[start]
                start += 1
            if summ == s:
                return [start + 1, end]
            summ += arr[end]
            end += 1
        return [-1]


# {
#  Driver Code Starts
# Initial Template for Python 3

import math


def main():
    T = 1
    while (T > 0):

        #NS = input().strip().split()
        N = 7
        S = 468

        A = [100, 36, 95, 104, 12, 123, 134]
        ob = Solution()
        ans = ob.subArraySum(A, N, S)
        print(sum(A[17:22]))
        for i in ans:
            print(i, end=" ")

        print()

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends