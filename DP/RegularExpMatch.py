def match(A, B, i, j):
    if i < 0 and j < 0:
        return True
    elif (i < 0 and j >= 0):
        for k in range(j + 1):
            if B[k] != '*':
                return False
        return True

    elif (j < 0 and i >= 0):
        for k in range(i+1):
            if A[k] != '*':
                return False
        return True
    sett = set(['*', '?'])
    if A[i] == B[j]:
        return match(A, B, i - 1, j - 1)
    elif A[i] not in sett and B[j] not in sett:
        return False
    else:
        if B[j] == '?' or A[i] == '?':
            return match(A, B, i - 1, j - 1)
        elif A[i] == '*' or B[j] == '*':
            return match(A, B, i - 1, j) or match(A, B, i, j - 1)

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def isMatch(self, A, B):
        n1 = len(A)

        n2 = len(B)
        ans = match(A, B, n1 - 1, n2 - 1)
        if ans is False:
            return 0
        else:
            return 1

s = Solution()
print(s.isMatch('aaaa', '***????'))