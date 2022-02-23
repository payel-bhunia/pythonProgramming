# User function Template for python3


class Solution:
    def MissingNumber(self, array, n):
        i=0
        while i < n-1:
            if array[i] != i + 1 and array[i] < n-1:
                ind = array[i] - 1
                array[i], array[ind] = array[ind], array[i]
                continue
            else:
                i+=1
        print(array)
        for i in range(n-1):
            if array[i] != i + 1:
                return i + 1
        return n

        # code here


# {
#  Driver Code Starts
# Initial Template for Python 3


t = 1
for _ in range(0, t):
    n = 7
    a = [2, 3, 4, 1, 6, 7]
    s = Solution().MissingNumber(a, n)
    print(s)
# } Driver Code Ends