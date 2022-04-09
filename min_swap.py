class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        start = 0
        end = len(A)-1
        count = 0
        while start <= end:
            while A[start] < B and start < len(A):
                start += 1
            while A[end] > B and end>-1:
                end -= 1
            if start < end:
                A[start],A[end]=A[end],A[start]
                count += 1
            else:
                break
        return count

A = [52, 7, 93, 47, 68, 26, 51, 44, 5, 41, 88, 19, 78, 38, 17, 13, 24, 74, 92, 5, 84, 27, 48, 3, 56, 79, 26, 55, 60, 16, 83, 63, 40, 55, 9, 96, 29, 7, 22, 11]
B = 19
s = Solution()
print(s.solve(A,B))