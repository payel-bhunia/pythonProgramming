class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        hash_map = {}
        n = len(A)
        for i in range(n):
            if A[i] not in hash_map:
                hash_map[(A[i],B[i])] = 1
            else:
                hash_map[(A[i],B[i])] += 1
        count = 0
        max_val = 0
        for i in range(n):
            for j in range(i+1,n):
                third1 = (A[i],B[j])
                third2 = (A[j],B[i])
                if third1 != (A[i],B[i]) and third1 != (A[j],B[j]):
                    if third1 in hash_map:
                        count += 1
                if third2 != (A[i], B[i]) and third2 != (A[j], B[j]):
                    if third2 in hash_map:
                        count += 1
            max_val = max(max_val,count)
        return max_val




A = [ 1, 1, 2, 3, 3 ]
B = [ 1, 2, 1, 2, 1 ]
s = Solution()
print(s.solve(A,B))