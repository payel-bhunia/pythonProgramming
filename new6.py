def solve(A):
    n = len(A)
    start = 0
    summ = 0
    i = 0
    max_sum = -1000000007
    while i < n:
        summ += A[i]
        i += 1
        if summ > max_sum:
            end = i
            max_sum = summ
        if summ < 0:
            summ = 0
            start = i
    print(max_sum)

if __name__ == "__main__":
    A = [2, 3, -1, 6, -10]
    solve(A)
