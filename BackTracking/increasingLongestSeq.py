# User function Template for python3
def find_seq(a, curr, max_len, size, idx, n, ans):
    if idx == n:
        if size > max_len[0]:
            max_len[0] = size
            ans.append(curr)
        return
    else:
        if len(curr) == 0:
            find_seq(a, curr.copy(), max_len, size, idx + 1, n, ans)
            curr.append(a[idx])
            size += 1
            find_seq(a, curr.copy(), max_len, size, idx + 1, n, ans)
            curr.pop()
            size -= 1
        else:
            if curr[-1] < a[idx]:
                find_seq(a, curr.copy(), max_len, size, idx + 1, n, ans)
                curr.append(a[idx])
                size += 1
                find_seq(a, curr.copy(), max_len, size, idx + 1, n, ans)
                curr.pop()
                size -= 1
            else:
                find_seq(a, curr.copy(), max_len, size, idx + 1, n, ans)




class Solution:

    # Function to find length of longest increasing subsequence.
    def longestSubsequence(self, a, n):
        idx = 0
        max_len = [0]
        size = 0
        curr = []
        ans = []
        find_seq(a, curr, max_len, size, idx, n, ans)
        print(ans)
        return max_len[0]

        # code here


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.longestSubsequence(a, n))
# } Driver Code Ends