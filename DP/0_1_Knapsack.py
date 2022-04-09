# User function Template for python3
def dp(wt, val, i, j, arr):
    if j == 0 or i == 0:
        return 0
    else:
        if arr[i][j] == -1:
            if wt[i-1] <= j:
                taken = dp(wt, val, i - 1, j - wt[i-1], arr)+val[i-1]
                arr[i - 1][j - wt[i-1]] = taken
            else:
                taken = 0
            nottaken = dp(wt, val, i - 1, j, arr)
            arr[i][j] = max(nottaken,taken)
        return arr[i][j]



class Solution:

    # Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self, W, wt, val, n):
        row = [-1] * (W+1)
        arr = []
        for i in range(2):
            arr.append(row.copy())
        #ans = dp(wt, val, i, j, arr)
        #return ans
        for i in range(n+1):
            for j in range(W+1):
                if i == 0 or j == 0:
                    arr[i][j] = 0
                else:
                    if wt[i-1] <= j:
                        arr[i][j] = max(arr[i-1][j], arr[i-1][j-wt[i-1]]+val[i-1])
                    else:
                        arr[i][j] = arr[i-1][j]
        return arr[n][W]




# {
#  Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys

if __name__ == '__main__':
    test_cases =1
    for cases in range(test_cases):
        n = 9#int(input())
        W = 383
        val = [ 359, 963, 465, 706, 146, 282, 828, 962, 492 ]#list(map(int, input().strip().split()))
        wt = [ 96, 43, 28, 37, 92, 5, 3, 54, 93 ]#list(map(int, input().strip().split()))
        #val = [60, 100, 120]
        #wt = [10,20,30]
        #W = 50
        #n = 3
        ob = Solution()
        print(ob.knapSack(W, wt, val, n))
# } Driver Code Ends