import math

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        if n < 3:
            return n
        max_val = 0
        dup = 0
        curr_val = 0
        ver = 0
        for i in range(n):
            dup = 0
            slope = {}
            curr_val=0
            ver = 0
            for j in range(i+1,n):
                if A[i]==A[j] and B[i] == B[j]:
                    dup += 1
                elif A[i]==A[j]:
                    ver += 1
                else:
                    dx = A[j]-A[i]
                    dy = B[j]-B[i]
                    gcd = math.gcd(dx,dy)
                    dx = dx/gcd
                    dy = dy / gcd
                    key = str(dx)+'__'+str(dy)
                    if key in slope:
                        slope[key] += 1
                    else:
                        slope[key] = 1
                    curr_val = max(curr_val,slope[key])
                curr_val = max(curr_val, ver)
            max_val = max(curr_val+dup+1,max_val)
        return max_val



A = [ 6, -5, 3, -6, 3, -9, -8, -7 ]
B = [ 5, 0, -8, 1, -1, 6, 3, -3 ]
s = Solution()
print(s.solve(A,B))