def min_diff(A,B):
    B.sort()
    A.sort()
    n = len(B)
    m = len(A)
    i = 0
    j = 0
    min_diff = 1000000007
    while i < n and i < m:
        if abs(A[i]-B[j]) < min_diff:
            min_diff = abs(A[i]-B[j])
            ans = (A[i], B[j])
        if A[i] < B[j]:
            i +=1
        elif A[i] > B[j]:
            j+=1
        else:
            return (A[i],B[j])
    return ans




if __name__ == "__main__":
    #A = list(map(int,input().split()))
    #B = list(map(int,input().split()))

    #case 1
    A = [-1,3,4,7,5]  #-1,3,4,5,7 i  mindiff
    B = [9,1,3,6,10]  # -3,-2,3,6,9,10 start  O(m+n)==O(N) + O(nlgn +nlgn) = O(2nlgn) = O(nlgn+mlgm)
    ans = min_diff(A, B)
    print(ans)
    # case 2
    A = [-1, 12, -3, 7, 19]  # -1,3,4,5,7
    B = [9, 1, -3, 8, 15]  # 1,3,6,9,10
    ans = min_diff(A, B)
    print(ans)
    # case 3
    A = [-1,5,10,20,28,3]  # -1,3,4,5,7
    B = [26,134,135,15,17]  # 1,3,6,9,10
    ans = min_diff(A, B)
    print(ans)
    A = [-1, 5, 10, 20, 28, 3]  # -1,3,4,5,7
    B = [26, 134, 3, 15, 17]  # 1,3,6,9,10
    ans = min_diff(A, B)
    print(A)
    print(ans)