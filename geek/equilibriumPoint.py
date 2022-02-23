# User function Template for python3

class Solution:
    # Complete this function

    # Function to find equilibrium point in the array.
    def equilibriumPoint(self, A, N):
        # Your code here
        right_sum = sum(A)
        left_sum = A[0]
        if left_sum == right_sum:
            return 1
        for i in range(1, N):
            if left_sum == right_sum:
                return i
            left_sum += A[i]
            right_sum -= A[i - 1]

        return -1


# {
#  Driver Code Starts
# Initial Template for Python 3

import math


def main():
    T = 1

    while (T > 0):
        N = 5

        A = [1,3,5,2,2]
        ob = Solution()

        print(ob.equilibriumPoint(A, N))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends