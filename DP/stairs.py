def ways(A,dp):
    if dp[A] == -1:
        dp[A] = ways(A-1,dp)+ways(A-2,dp)
    return dp[A]

#User function Template for python3
def ways_ord_not_Imp(m,ans,i):
    if i > 2:
        return 0
    if m == 0:
        return 1
    elif m < 0:
        return 0
    if ans[m][i] != -1:
        return ans[m][i]
    else:
        if m == 1 and i == 0:
            return 1
        if m == 2 and i == 0:
            return 2
        ans[m][i] = ways_ord_not_Imp(m,ans,i+1)+ways_ord_not_Imp(m-i,ans,i)
        return ans[m][i]
class Solution:
    def climbStairs(self, A):
        if A == 1:
            return 1

        else:
            dp = []
            col = [-1]*3
            for i in range(A+1):
                dp.append(col.copy())
            #ans = ways(A,dp)
            ans1 = ways_ord_not_Imp(A,dp,1)
            #return ans1
            return ans1



if __name__ == '__main__':
    A = 4
    s = Solution()
    ans = s.climbStairs(A)
    print(ans)