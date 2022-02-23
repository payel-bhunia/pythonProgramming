# User function Template for python3

class Solution:
    def indexes(self, v, x):
        n = len(v)
        start = 0
        end = len(v) - 1
        idx_s = -1
        idx_e = -1
        while start <= end:
            mid = start + (end - start) // 2
            if v[mid] > x:
                end = mid - 1
            elif v[mid] < x:
                start = mid + 1
            else:
                idx_s = mid
                idx_e = mid
                break
        if idx_s != -1:
            while idx_s > -1:
                if v[idx_s] == x:
                    if idx_s == 0:
                        break
                    idx_s -= 1
                else:
                    idx_s += 1
                    break
            while idx_e < n:
                if v[idx_e] == x:
                    if idx_e == n - 1:
                        break
                    idx_e += 1
                else:
                    idx_e -= 1
                    break
        return [idx_s, idx_e]

        # Your code goes here


# {
#  Driver Code Starts
# Initial Template for Python 3

def main():
    T = 1

    while (T > 0):
        n = 9
        a = [1, 3, 5, 5, 5, 5, 67, 123, 125]
        k = 5
        obj = Solution()
        ans = obj.indexes(a, k)
        if ans[0] == -1 and ans[1] == -1:
            print(-1)
        else:
            print(ans[0], end=' ')
            print(ans[1])

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends