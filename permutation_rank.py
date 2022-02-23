# User function Template for python3
def check_rank(A):
    start = A[0]
    fact = len(A) - 1
    fact_val = 1
    count = 0
    for i in range(1, len(A)):
        if ord(start) > ord(A[i]):
            count += 1
    if count > 0:
        while fact > 0:
            fact_val *= fact
            fact -= 1
        return count * fact_val
    else:
        return 0


class Solution:
    def rank(self, S):
        if len(S) > 26:
            return 0
        rnk = 1
        for i in range(len(S)):
            rnk += check_rank(S[i:])
        return rnk


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    #t = int(input())
    #for _ in range(t):
    #    S = input()
    S = 'dcba'
    ob = Solution()
    print(ob.rank(S))
# } Driver Code Ends