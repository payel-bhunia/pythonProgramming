def solve(A):
    n = len(A)
    l = [0] * 26
    for i in A:
        index = ord(i) - ord('a')
        l[index] += 1
    max_count = max(l)
    if max_count > (n+1)//2:
        return False
    else:
        /