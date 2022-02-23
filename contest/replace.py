class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        hash_map = {}
        for i in range(len(B)):
            if B[i][0] != B[i][1]:
                hash_map[B[i][0]] = B[i][1]

        i = 0
        while i < len(A):
            if A[i] in hash_map:
                A[i] = hash_map[A[i]]
            else:
                i += 1
        return A

if __name__ == '__main__':
    A = [2,2,5,1]
    B = [[3,2],[5,5],[2,4],[3,2],[5,2]]
    s = Solution()
    ans = s.solve(A,B)
    print(ans)