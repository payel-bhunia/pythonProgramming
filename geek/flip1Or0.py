# User function Template for python3

class Solution:
    def maxOnes1(self, a, n):
        ans = []
        start = 0
        max_len = 0
        leng = 0
        flag = 0
        for i in range(n):
            if a[i] == 0:
                if flag == 0:
                    leng = 0
                    start = i
                    flag = 1
                leng += 1
                if leng > max_len:
                    max_len = leng
                    end = i
                    ans = [start, end]
            else:
                leng -= 1
            if leng < 0:
                flag = 0
        if len(ans):
            start = ans[0]
            end = ans[1]
        else:
            start = end = -1
        print(ans, max_len)
        leng = 0
        for i in range(n):
            if i >= start and i <= end:
                if a[i] == 0:
                    leng += 1
            else:
                if a[i] == 1:
                    leng += 1
        return leng

        # Your code goes here
#User function Template for python3
#User function Template for python3

class Solution:
    def maxOnes(self, a, n):
        ans = []
        start = 0
        end = -1
        max_len = 0
        leng = 0
        flag = 0
        for i in range(n):
            if a[i] == 0:
                if flag == 0:
                    start = i
                    flag = 1
                leng += 1
                if leng > max_len:
                    max_len = leng
                    end = i
                    ans = [start,end]
            else:
                leng -= 1
            if leng < 0:
                flag = 0
        if len(ans):
            start = ans[0]
            end = ans[1]
        else:
            start = end = -1
        print(ans,max_len)
        leng = 0
        for i in range(n):
            if i >= start and i <= end:
                if a[i] == 0:
                    leng += 1
            else:
                if a[i] == 1:
                    leng += 1
        return leng


# {
#  Driver Code Starts
# Initial Template for Python 3

def main():
    T = 1

    while (T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.maxOnes(a, n))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends