def solve(a, b):
    n = len(a)
    pref_sum = [a[0]] * n
    for i in range(1, n):
        pref_sum[i] = pref_sum[i-1] + a[i]
    max_sum = pref_sum[b-1]
    curr_sum = max_sum
    for i in range(b):
        right_sum = pref_sum[b-1-i]
        left_sum = pref_sum[n-1] - pref_sum[n-1-i]
        curr_sum = right_sum + left_sum
        if curr_sum > max_sum:
            max_sum = curr_sum
    left_sum = pref_sum[n-1] - pref_sum[n-1-b]
    curr_sum = left_sum
    if curr_sum > max_sum:
        max_sum = curr_sum
    return max_sum


if __name__ == '__main__':
    A = [5, -1, 3, 1, 1, 4, -1]
    B = 3
    solve(A, B)



