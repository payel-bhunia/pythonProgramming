# User function Template for python3

class Solution:
    def printKClosest(self, arr, n, k, x):
        start = 0
        end = n - 1
        exact = -1
        prev = -1
        nxt = -1
        ans = []
        count = 0
        while start <= end:
            mid = start + (end - start) // 2
            if arr[mid] > x:
                nxt = mid
                end = mid - 1
            elif arr[mid] < x:
                prev = mid
                start = mid + 1
            else:
                exact = mid
                break
        if exact != -1:
            prev = exact - 1
            nxt = exact + 1

        while prev > -1 and nxt < n:
            if x - arr[prev] < arr[nxt] - x:
                ans.append(arr[prev])
                prev -= 1
            elif x - arr[prev] > arr[nxt] - x:
                ans.append(arr[nxt])
                nxt += 1
            else:
                ans.append(arr[nxt])
                nxt += 1
            count += 1
            if count == k:
                return ans
        while prev > -1 and count < k:
            ans.append(arr[prev])
            prev -= 1
            count += 1
        while nxt < n and count < k:
            ans.append(arr[nxt])
            nxt += 1
            count += 1
        return ans

        # code here


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = 1
    while tc > 0:
        n = 5
        arr = [1,2,3,6,10]
        k, x = 3,4
        ob = Solution()
        ans = ob.printKClosest(arr, n, k, x)
        for xx in ans:
            print(xx, end=" ")
        print()
        tc -= 1

# } Driver Code Ends

