# User function Template for python3
class Solution:
    def calculateMaxSumLength(self, arr, n, k):
        flag = 0
        leng = 0
        summ_leng = 0
        for i in range(n):
            if arr[i < k:
                leng += 1
            elif i == k:
                leng += 1
                flag = 1
            else:
                if flag == 1:
                    print(arr[i], leng, summ_leng)
                    summ_leng += leng
                    flag = 0
                leng = 0
        if flag == 1:
            summ_leng += leng
        return summ_leng

        # Your code goes here


# {
#  Driver Code Starts
if __name__ == '__main__':

    t = 1
    for _ in range(0, t):
        n = int(input())
        a = list(map(int, input().split()))
        k = int(input())
        ob = Solution()
        ans = ob.calculateMaxSumLength(a, n, k)
        print(ans)
# } Driver Code Ends