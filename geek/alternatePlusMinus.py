#User function Template for python3

class Solution:
    def rearrange(self,arr, n):
        # code here
        ans1 = []
        ans2 = []
        for i in range(n):
            if arr[i] >= 0:
                ans1.append(arr[i])
            else:
                ans2.append(arr[i])
        i = 0
        j = 0
        idx = 0
        print(ans1)
        print(ans2)
        while i<len(ans1) and j<len(ans2):
            if i&1 == 0:
                arr[idx] = ans1[i]
                i+=1
            else:
                arr[idx] = ans2[j]
                j+=1
            idx+=1
        while i<len(ans1):
            arr[idx] = ans1[i]
            i+=1
            idx += 1
        while j < len(ans2):
            arr[idx] = ans2[j]
            j+=1
            idx += 1
        return arr

#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = 1
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.rearrange(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends