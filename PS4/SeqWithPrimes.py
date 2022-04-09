'''Smallest sequence with given Primes'''
'''Given three prime number(A, B, C) and an integer D. 
Find the first(smallest) D integers which have only A, B, C or a combination of them as their prime factors.'''


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return a list of integers
    def solve(self, A, B, C, D):
        ia = ib = ic = 0
        (clA, clB, clC) = (A, B, C)
        ans = [1]
        while D > 0:
            min_val = min(clA, clB, clC)
            ans.append(min_val)
            if clA == min_val:
                ia += 1
                clA = A * ans[ia]
            if clB == min_val:
                ib += 1
                clB = B * ans[ib]
            if clC == min_val:
                ic += 1
                clC = C * ans[ic]
            D -= 1
        return ans[1:]



s = Solution()
print(s.solve(2,3,5,5))