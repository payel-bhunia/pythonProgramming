def solve(A):
    n = len(A)
    left_max = [A[0]] * n
    right_max = [A[-1]] * n
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], A[i])
    i = n-2
    while i >= 0:
        right_max[i] = max(right_max[i+1], A[i])
        i -= 1
    ans = 0
    for i in range(len(A)):
        if A[i] < left_max[i] and A[i] < right_max[i]:
            ans += min(left_max[i], right_max[i]) - A[i]
    return ans


if __name__ == '__main__':
    A = [5, 1, 3, 1, 1, 4, 0]
    n = solve(A)
    print(n)
