def solve(k):
    ans = [0] * (k+1)
    if k == 1:
        return [1]
    elif k == 2:
        return [1, 1]
    else:
        ans[0] = 1
        ans[1] = 1
        for i in range(2, k+1):
            prev = ans.copy()
            for j in range(1, i):
                ans[j] = prev[j-1] + prev[j]
            ans[i] = 1
        return ans


def main():
    k = 5
    n = solve(k)
    print(n)


if __name__ == '__main__':
    main()




