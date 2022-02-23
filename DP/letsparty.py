#UDDDUDUDUUUUDDUUDUDUDUDUDD

def solve(A):
    n = len(A)
    pref = [0] * n
    if A[0] == 'U':
        pref[0] = 1
    else:
        pref[0] = -1

    for i in range(1,n):
        if A[i] == 'D':
            pref[i] = pref[i-1] - 1
        else:
            pref[i] = pref[i - 1] + 1
    i = 0
    peak = 0
    vall = 0
    print(pref)
    while i < n:
        if pref[i] == 0:
            end = i
            break
        else:
            if pref[i] < 0:
                vall = 1
            else:
                peak = 1
            i += 1
    while end < n:
        if pref[end] == 0:
            if end+1 < n:
                if pref[end+1] > 0:
                    peak += 1
                else:
                    vall += 1
            end = end +1
        else:
            end += 1
    print(peak,vall)

if __name__ == "__main__":
    #A = 'UDDDUDUDUUUUDDUUDUDUDUDUDD'
    A = 'DUUDDDUDUDUUUUDDUUDUDUDUDUDDUDDDUDUDUUUUDDUUDUDUDUDUDD'
    solve(A)







