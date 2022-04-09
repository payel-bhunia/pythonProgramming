class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        A_sort = sorted(A)
        hash_map = {}
        for i in range(len(A)):
            if A[i] in hash_map:
                hash_map[A[i]].append(B[i])
            else:
                hash_map[A[i]] = [B[i]]
        j = 0
        while j < len(A_sort):
            n = len(hash_map[A_sort[j]])
            for k in range(n):
                B[j] = hash_map[A_sort[j]][k]
                j += 1
        cl = [B[0]]
        t = 1
        profit = B[0]
        for i in range(1,len(A)):
            if t < A_sort[i]:
                cl.append(B[i])
                profit += B[i]
                t += 1
            else:
                if t-1 < A_sort[i] and min(cl)<B[i]:
                    minn = min(cl)
                    cl.remove(minn)
                    cl.append(B[i])
                    profit -= minn
                    profit += B[i]
        return profit




s = Solution()
A = [1, 3, 2, 3, 3]
B = [5, 6, 1, 3, 9]
print(s.solve(A,B))