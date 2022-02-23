def flip(A):
    start = -1
    end = -1
    count_r = 0
    count_l = 0
    A = A + 'n'
    state = 0
    hash_map = {}
    max_size = -1
    for i in range(len(A)):
        if A[i] == '0':
            if state == 0:
                if count_r != 0:
                    if start != -1:
                        size = count_l + (end-start+1) + count_r
                        if size not in hash_map:
                            hash_map[size] = [start+1, end+1]
                        max_size = max(size, max_size)
                    count_l = count_r
                    count_r = 0
                start = i
                end = i
                state = 1
            else:
                end += 1
        elif A[i] == '1':
            if state == 1:
                state = 0
            count_r += 1
        else:
            if start != -1:
                size = count_l + (end-start+1) + count_r
                if size not in hash_map:
                    hash_map[size] = [start + 1, end + 1]
                max_size = max(size, max_size)
    if start == -1 and end == -1:
        return []
    else:
        return hash_map[max_size]


def main():
    k = '0001000'
    n = flip(k)
    print(n)


if __name__ == '__main__':
    main()





