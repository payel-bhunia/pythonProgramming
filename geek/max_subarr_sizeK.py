# User function Template for python3

class Solution:

    # Function to find maximum of each subarray of size k.
    def max_of_subarrays(self, arr, n, k):

        cl = []
        ans = []
        for i in range(k):
            if len(cl) == 0:
                cl.append(arr[i])
            else:
                while len(cl):
                    if cl[-1] < arr[i]:
                        cl.pop()
                    else:
                        break
                cl.append(arr[i])
        start = 0
        end = k
        ans.append(cl[0])
        while end < n:
            print(arr[start+1:end+1])
            if arr[start] == cl[0]:
                cl.pop(0)
            start += 1
            if len(cl) == 0:
                cl.append(arr[end])
            else:
                while len(cl):
                    if cl[-1] < arr[end]:
                        cl.pop()
                    else:
                        break
                cl.append(arr[end])
            while len(cl) > k:
                cl.pop(0)
            ans.append(cl[0])
            print('max_value=',ans[-1])
            print(cl)
            end += 1
        return ans




if __name__ == '__main__':
    test_cases = 1
    for cases in range(test_cases):
        k = 6
        arr = [2,4,5, 2, 3, 7, 8, 5, 4, 4, 4, 6, 3, 9, 8, 1, 2, 4, 6, 9]
        n = len(arr)
        ob = Solution()
        res = ob.max_of_subarrays(arr, n, k)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()
# } Driver Code Ends