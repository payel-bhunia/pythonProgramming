def solve(A, k):
    n = len(A)
    start = 0
    end = k
    sum = 0
    for i in range(k):
        sum += A[i]
    min_val = sum
    while end < n:
        sum -= A[start]
        sum += A[end]
        start += 1
        end += 1
        min_val = min(min_val, sum)
    return min_val


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5]
    n = solve(A, 3)
    print(n)


