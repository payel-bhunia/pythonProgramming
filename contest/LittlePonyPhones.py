class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        n = len(A)
        ans = []
        for i in range(1, n):
            A[i] = A[i - 1] + A[i]
        C = sorted(B)
        hash_map = dict()
        prev = -1
        for i in range(n):
            if A[i] <= C[0]:
                prev = i
            else:
                hash_map[C[0]] = prev + 1
                break
        if prev == -1:
            start = 0
        else:
            start = prev
        i = 1
        while start < n:
            if A[start] <= C[i]:
                prev = start
                start += 1
            else:
                hash_map[C[i]] = prev + 1
                start = prev
                i += 1
        while i < len(B) and start == n:
            hash_map[C[i]] = n
            i += 1
        for i in B:
            ans.append(hash_map[i])

        return ans



if __name__ == '__main__':
    tc = 1
    while tc > 0:
        A = [23,36,58,59]
        B = [3,207,62,654,939,680,760]
        ob = Solution()
        ans = ob.solve(A,B)
        print(ans)
        tc -= 1