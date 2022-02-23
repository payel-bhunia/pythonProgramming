def solve(A, B):
    n = len(A)
    start = 0
    ans = []
    if n < B:
        return []
    else:
        end = 0
        count = 0
        hash_map = {}
        while end < B:
            if A[end] not in hash_map:
                hash_map[A[end]] = 1
                count += 1
            else:
                hash_map[A[end]] += 1
            end += 1
        end = B
        ans.append(count)
        while end < n:
            if A[start] != A[end]:
                if hash_map[A[start]] == 1:
                    count -= 1
                    hash_map.pop(A[start])
                else:
                    hash_map[A[start]] -= 1
                if A[end] in hash_map:
                    hash_map[A[end]] += 1
                else:
                    hash_map[A[end]] = 1
                    count += 1
            ans.append(count)
            start += 1
            end += 1
        return ans


if __name__ == '__main__':
    A = [1, 1, 2, 2]
    B = 1
    n = solve(A, B)
    print(n)



