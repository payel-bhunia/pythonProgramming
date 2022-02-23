def solve(A, k):
    n = len(A)
    hash_set = set()
    for i in range(n):
        hash_set.add(A[i])
    arr = list(hash_set)
    arr.sort()
    hash_map ={}
    n1 = len(Arr)
    for i in range(n1):
        hash_map[arr[i]] = n1 - 1 - i
    for i in range(n):
        if 