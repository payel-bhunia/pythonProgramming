# User function Template for python3

class Solution:

    # Function to return a list containing the union of the two arrays.
    def mergeArrays(self, a, b, n, m):
        ans = []
        start1 = 0
        start2 = 0
        idx = -1
        while start1 < n and start2 < m:
            if a[start1] != b[start2]:
                if a[start1] < b[start2]:
                    val = a[start1]
                    start1 += 1
                else:
                    val = b[start2]
                    start2 += 1
            else:
                val = a[start1]
                start1 += 1
                start2 += 1

            if idx > -1:
                if ans[idx] != val:
                    ans.append(val)
                    idx += 1
            else:
                ans.append(val)
                idx += 1
        while start2 < m:
            if idx > -1:
                if ans[idx] != b[start2]:
                    ans.append(b[start2])
                    idx += 1
            else:
                ans.append(b[start2])
                idx += 1
            start2 += 1
        while start1 < n:
            if idx > -1:
                if ans[idx] != a[start1]:
                    ans.append(a[start1])
                    idx += 1
            else:
                ans.append(a[start1])
                idx += 1
            start1 += 1
        return ans


()
# {
#  Driver Code Starts
# Initial Template for Python 3

# Contributed by : Nagendra Jha
# Modified by : Sagar Gupta


if __name__ == '__main__':
    test_cases = 1
    for cases in range(test_cases):
        n, m = map(int, input().strip().split())
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        ob = Solution()
        li = ob.mergeArrays(a, b, n, m)
        for val in li:
            print(val, end=' ')
        print()
# } Driver Code Ends