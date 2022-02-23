def maxSubArray(A):
    cur_sum = A[0]
    max_sum = A[0]
    start = 0
    end = 0
    pair = []
    for i in range(1, len(A)):
        if A[i] > 0:
            cur_sum += A[i]
        else:
            cur_sum = max(cur_sum + A[i], A[i])
        if cur_sum > max_sum:
            max_sum = cur_sum
            end = i
            pair = [start + 1, end + 1]
        if cur_sum < 0:
            cur_sum = 0
            start = i + 1
    return pair


def main():
    k = [2, 3, -1, 6, -10]
    n = maxSubArray(k)
    print(n)


if __name__ == '__main__':
    main()



