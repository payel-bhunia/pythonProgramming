def flip(A):
    hash_map = {}
    l = 0
    r = 0
    state = 0
    count_1 = 0
    size = 0
    max_size = size
    A = A + 'n'
    for i in range(len(A)):
        if A[i] == '0':
            if state == 0:
                size = r - l + 1 + count_1
                if size not in hash_map:
                    hash_map[size] = [l, r]
                max_size = max(max_size, size)
                l = i
                state = 1
                r = i
            else:
                r += 1
        elif A[i] == '1':
            if state == 1:
                state = 0
                count_1 = 1
            else:
                count_1 += 1
        else:
            size = r - l + 1 + count_1
            if size not in hash_map:
                hash_map[size] = [l, r]
            max_size = max(max_size, size)
    if max_size != 0:
        return hash_map[max_size]
    else:
        return []


def main():
    k = '11010001111'
    n = flip(k)
    print(n)


if __name__ == '__main__':
    main()

