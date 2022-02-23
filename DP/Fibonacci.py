def fib(n, dp):
    print(n, dp)
    if dp[n] != -1:
        return dp[n]
    else:
        dp[n] = fib(n - 1, dp) + fib(n - 2, dp)
        return dp[n]

def fibo(n):
    prev1 = 0
    prev2 = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(2,n+1):
            ans = prev1+prev2
            prev1 = prev2
            prev2 = ans
        return ans


def main():
    n = int(input())
    dp = [-1] * (n + 1)
    dp[1] = 0
    dp[2] = 1
    #ans = fib(n, dp)
    ans = fibo(n)
    print(ans)


if __name__ == '__main__':
    main()
