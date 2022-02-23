def kthsmallest(A, B):
    n = len(A)
    C = list(A)
    for i in range(B):
        x = C[i]
        pos = i
        for j in range(i, n, 1):
            if C[j] < x:
                pos = j
                x = C[j]
        if pos != i:
            C[i], C[pos] = C[pos], C[i]
    return C[B - 1]

if __name__ == "__main__":
    A = (8, 16, 80, 55, 32, 8, 38, 40, 65, 18, 15, 45, 50, 38, 54, 52, 23, 74, 81, 42, 28, 16, 66, 35, 91, 36, 44, 9, 85, 58, 59, 49, 75, 20, 87, 60, 17, 11, 39, 62, 20, 17, 46, 26, 81, 92)
    print(sorted(A))
    val = kthsmallest(A, 8)
    print(val)

   # 2 3 5 6 8 9