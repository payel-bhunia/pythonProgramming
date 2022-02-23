# User function Template for python3

class Solution:
    def countEleLessThanOrEqual(self, arr1, n1, arr2, n2):
        arr2.sort()
        ans = []
        for i in arr1:
            start = 0
            end = n2 - 1
            prev = -1
            flag = 0
            while start <= end:
                mid = start + (end - start) // 2
                if i < arr2[mid]:
                    end = mid - 1
                elif i > arr2[mid]:
                    prev = mid
                    start = mid + 1
                else:
                    flag = 1
                    break
            if flag == 1:
                while mid < n2:
                    if arr2[mid] == i:
                        mid += 1
                    else:
                        break
                ans.append(mid)
            else:
                if prev == -1:
                    ans.append(0)
                else:
                    ans.append(prev + 1)
        return ans

        # returns the required output


# {
#  Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
if __name__ == '__main__':
    t = 1

    for tcs in range(t):

        n1, n2 = [int(x) for x in input().split()]
        arr1 = [int(x) for x in input().split()]
        arr2 = [int(x) for x in input().split()]

        res = Solution().countEleLessThanOrEqual(arr1, n1, arr2, n2)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()
# } Driver Code Ends