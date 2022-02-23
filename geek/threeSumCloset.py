# User function Template for python3

# arr    : list of integers denoting the elements of the array
# target : as specified in the problem statement

class Solution:
    def threeSumClosest(self, arr, target):
        # Your Code Here
        min_diff = 1000000007
        arr.sort()
        n = len(arr)
        ans = sum(arr[:3])
        for i in range(n):
            summ = target - arr[i]
            start = i + 1
            end = n - 1
            while start < end:
                diff = summ - arr[start] - arr[end]
                if abs(diff) < min_diff:
                    min_diff = abs(diff)
                    ans = arr[start] + arr[end] + arr[i]
                elif abs(diff) == min_diff:
                    if ans < arr[start] + arr[end] + arr[i]:
                        ans = arr[start] + arr[end] + arr[i]
                if diff > 0:
                    start += 1
                elif diff < 0:
                    end -= 1
                else:
                    return target

        return ans


# {
#  Driver Code Starts
# Initial Template for Python 3

t = 1
for tc in range(t):
    n, target = list(map(int, input().split()));
    arr = list(map(int, input().split()));

    print(Solution().threeSumClosest(arr, target))

# } Driver Code Ends